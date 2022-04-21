def find_files(suffix, path="."):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    import os

    #null check for path and suffix
    if len(suffix) <= 256 and len(path) <= 256:
      if os.path.isfile(path):
        #print(path)
        if path.endswith(suffix):
          print(path)
      elif os.path.isdir(path):
        subdirectories = os.listdir(path)
        for directory in subdirectories:
          find_files(suffix, os.path.join(path,directory))
    else:
      print("file path exceeded length of 256")

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
#suffix is null
find_files("./testdir")

# Test Case 2
#directory is null
find_files(".c")

# Test Case 3
#too long of a path
#catcn windows limit of 256 characters
find_files("Users\wumpus-home\AppData\Local\Packages\WinStore_cw5n1h2txyewy\AC\Microsoft\Windows Store\Cache\0\0-Namespace-https???services.apps.microsoft.com?browse?6.2.9200-1?615?en-US?c?US?Namespace?pc?00000000-0000-0000-0000-000000000000?00000000-0000-0000-0000-000000000000", "testdir")

#OS Module Exploration Code
## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

