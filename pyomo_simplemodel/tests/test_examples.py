import pyutilib.th as unittest
import os
import os.path
import glob
import sys

currdir = os.path.dirname(os.path.realpath(__file__))
testdir=os.path.abspath(os.path.join(currdir, '..', '..', 'examples'))

class TestExamples(unittest.TestCase): pass

cwd = os.getcwd()
os.chdir(testdir)

for file_ in glob.glob('*.py'):
    bname = os.path.basename(file_)
    dir_ = os.path.dirname(os.path.abspath(file_))+os.sep
    name='.'.join(bname.split('.')[:-1])
    tname = name
    cmd = '%s %s' % (sys.executable, os.path.abspath(bname))
    #sys.stderr.write("DIR: %s\n" % dir_)
    #sys.stderr.write("CMD: %s\n" % cmd)
    if os.path.exists(dir_+name+'.txt'):
        TestExamples.add_baseline_test(cmd=cmd,  baseline=dir_+name+'.txt', name=tname, tolerance=1e-7, cwd=cwd)
    elif os.path.exists(dir_+name+'py%d.txt' % sys.version_info[0]):
        TestExamples.add_baseline_test(cmd=cmd,  baseline=dir_+name+'.py%d.txt' % sys.version_info[0], name=tname, tolerance=1e-7, cwd=dir_)

os.chdir(cwd)

# Execute the tests
if __name__ == '__main__':
    unittest.main()
