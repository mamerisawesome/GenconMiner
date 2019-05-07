from subprocess import check_call

def jupyter() -> None:
    check_call([ "jupyter", "lab", "--NotebookApp.token=''", "--no-browser" ])
