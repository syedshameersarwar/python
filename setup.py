from cx_Freeze import setup, Executable

base = None    

executables = [Executable("SimilarityChecker.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Similarity Checker",
    options = options,
    version = "0.1",
    description = '',
    executables = executables
)
