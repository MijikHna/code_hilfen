### C++, Python, Java in VS Code
1. Erweiterungen:
    1. C/C++
    2. C++ Intellisense
    3. Python 
    4. Java Extention Pack
    5. Code Runner
2. in Settings:
    1. Code-Runner:Run in Terminal: true
    2. Code-Runner:Executor Map: `"code-runner.executorMap": {    "cpp": "cd $dir && g++ -std=c++14 $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt"}`
3. jetzt mit Rechts Klick -> Run Code