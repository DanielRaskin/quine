def quine_print(s):
    print(s + "quine_print(\"" + s.replace("\\", "\\\\").replace("\n", "\\n").replace("\"", "\\\"") + "\")")


quine_print("def quine_print(s):\n    print(s + \"quine_print(\\\"\" + s.replace(\"\\\\\", \"\\\\\\\\\").replace(\"\\n\", \"\\\\n\").replace(\"\\\"\", \"\\\\\\\"\") + \"\\\")\")\n\n\n")
