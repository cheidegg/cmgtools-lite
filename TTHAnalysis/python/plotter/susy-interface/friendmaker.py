import os
from optparse import OptionParser
from lib import maker
from lib import functions as func

def collectFriends(modulelist):
	if len(modulelist)==0: return ""
	return " ".join(["-F sf/t {P}/"+m+"/evVarFriend_{cname}.root" for m in modulelist])

def getFriendConn(mm, module):
	friendConn = mm.getVariable("friendConn")
	if module in friendConn.keys():
		return friendConn[module]
	return []

def getFriendFile(mm, module):
	friendFile = mm.getVariable("friendFile")
	if module in friendFile.keys(): 
		return friendFile[module][0]
	return ""


parser = OptionParser(usage="%prog cfg regions treedir outdir [options]")
parser = maker.addMakerOptions(parser)
parser.add_option("--modules"     , dest="modules", type="string", action="append", default=[], help="Semicolon-separated list of modules to run")
parser.add_option("--exclude"     , dest="exclude", type="string", action="append", default=[], help="Semicolon-separated list of samples to exclude (regexp)")
parser.add_option("--accept"      , dest="accept" , type="string", action="append", default=[], help="Semicolon-separated list of samples to accept (regexp)")
parser.add_option("--direct"      , dest="direct" , action="store_true", default=False, help="Do direct batch submission (default is doing the batch submission via prepareEventVariablesFriendTree.py) [useful for splitted fastsim masspoints]")
parser.add_option("--bk"          , dest="bk"     , action="store_true", default=False, help="Bookkeeping option (stores friend tree producer and configuration)")
parser.add_option("--log"         , dest="log"    , action="store_true", default=False, help="Put log file into subdirectory 'log' in output directory")
parser.add_option("-F", "--force" , dest="force"  , action="store_true", default=False, help="Run the module even if it already exists")

base = "python prepareEventVariablesFriendTree.py {T} {O} --tree {TREENAME} --vector -T sf -d {SAMPLES} -m {MODULES} {FRIENDS} {ADDITIONAL}"
(options, args) = parser.parse_args()
options         = maker.splitLists(options)
options.modules = func.splitList(options.modules)
options.accept  = func.splitList(options.accept )
options.exclude = func.splitList(options.exclude)
mm              = maker.Maker(base, args, options)
mm.workdir      = mm.cmssw +"/src/CMGTools/TTHAnalysis/macros"
mm.loadNEvtSample()


## loop on modules
for module in mm.getFriendModules():

	output = mm.outdir +"/"+ module
	func.mkdir(output)
	func.mkdir(output +"/log")
	if options.bk: func.mkdir(output +"/ref")

	file     = getFriendFile(mm, module)
	requires = getFriendConn(mm, module)
	requires = filter(lambda x: x, requires)


	## loop on samples
	for d in os.listdir(mm.treedir):

		## only consider real samples
		if not os.path.isdir(mm.treedir +"/"+ d): continue
		if not os.path.exists(mm.treedir +"/"+ d +"/"+options.treename+"/tree.root") and \
           not os.path.exists(mm.treedir +"/"+ d +"/"+options.treename+"/tree.root.url"): continue

		## exclude or accept
		if options.accept  != [] and all([d.find(a) == -1 for a in options.accept ]): continue
		if options.exclude != [] and any([d.find(e) >  -1 for e in options.exclude]): continue

		## check if required friend trees exist
		passed = True
		for req in requires:
			if req and not os.path.exists(mm.treedir +"/"+ req +"/evVarFriend_"+d+".root"): 
				print "WARNING: required friend tree module '"+req+"' for module '"+module+"' does not exist for sample '"+d+"'"
				print "Skipping..."
				passed = False
		if not passed: continue

		## skip if exists (and not force recreation)
		if not options.force and os.path.exists(mm.treedir +"/"+ module +"/evVarFriend_"+d+".root"): continue


		## submit
		friends    = collectFriends(requires)
		additional = "--bk" if options.bk else ""
	
		if not options.direct and options.queue:
			nevt        = mm.getNEvtSample(d)
			additional += " -N "+nevt if nevt else ""
			additional += " -q "+ options.queue
			if options.queue in ["all.q", "long.q", "short.q"]: additional += " --env psi"
			if options.log: additional += " --log "+output+"/log"

		mm.submit([mm.treedir, output, options.treename, d, module, friends, additional])

	if options.bk:
		func.cp(mm.cmssw+"/src/CMGTools/TTHAnalysis/macros/prepareEventVariablesFriendTree.py", output+"/ref")
		func.cp(mm.cmssw+"/src/CMGTools/TTHAnalysis/python/tools/"+file                       , output+"/ref")
	

	


