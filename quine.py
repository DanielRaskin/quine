def quine_print(s):
    print(s + "s = \"" + s.replace("\\", "\\\\").replace("\n", "\\n").replace("\"", "\\\"") + "\"\nquine_print(s)")


s = "def quine_print(s):\n    print(s + \"s = \\\"\" + s.replace(\"\\\\\", \"\\\\\\\\\").replace(\"\\n\", \"\\\\n\").replace(\"\\\"\", \"\\\\\\\"\") + \"\\\"\\nquine_print(s)\")\n\n\n"
quine_print(s)
