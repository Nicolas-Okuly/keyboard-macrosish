#Requires AutoHotkey v2

RAlt:: {
    ih := InputHook("L0 I1")
    ih.KeyOpt("{All}", "ES")
    ih.Start()

    reason := ih.Wait()

    key := ih.EndKey

    if (key != "") {
        home := EnvGet("USERPROFILE") 
        Script := home . "\ahk-macros.py"
        Run('pythonw.exe "' . Script . '" "' . key . '"')
    }
}