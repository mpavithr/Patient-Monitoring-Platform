from entering_in_shell import shell:
  
  def test_shell_empty():
    if shell.firstName == "":
      assert shell.user["firstName"] == None
