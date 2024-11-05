# SuperUtilities-Python3
A custom made python 3 file that adds some features that aim to streamline the coding process.

This was made primarily for a python coding class, apologies it is a little out of the blue.

### Installation:
`pip install superutilities`

### Functions:

- **SInput**: A beefed up version of input(), has built in error handling, allows for automatic type conversion and retries, along with gui support.
  - prompt:str - The prompt you wish to ask the user.
  - IsInt:bool - Should the user's input be a returned as an integer?
  - IsBool:bool - Should the user's input be a returned as a bool?
  - IsFloat:bool - Should the user's input be a returned as a float?
  - acceptedAnswers:list - List of accepted answers. If list is not empty it will ask the user to retry if input is not in this list.
  - AACaseSensitive:bool - If accepted answers should be case-sensitive.
  - UseRegularExpression:bool - Use regex to determine if the input is valid or not. (See RegularExpression variable to set regex.)
  - RegularExpression - The regex to use if the input is valid. `r''`
  - ReturnREListOnly:bool - Bypasses ALL other arguments and returns a list of accepted inputs found by regex.
  - printBypass:bool - Disables the print function.
  - inputBypass - The user's input given by a separate function (For use in GUI environments).
  - useInputBypass:bool - Should the function use the input given from the inputBypass argument.
 

- **SanitizeString**: A function that removes, strips, and detects certain combinations of strings or regex within other strings. Built with the idea of being used to prevent inputs that could lead to unintended outputs.
  - string:str - The string to sanitize.
  - TestFor:bool - Returns true if it finds a 'banned character' in the string.
  - PrintFound:bool - Makes TestFor return the characters found in the string. (Must have TestFor set to true for it to have any effect)
  - bannedCharacters:list - A list of strings of banned characters to remove from the string.
  - replaceWith: - A string to replace sanitized characters with. Default is nothing.


- **PermutationCalculator**: A small function that returns the number of possible combinations of certain points and values.
  - NumOfPoints:int - Number of points/spots for a value to be.
  - NumOfValues:int - Number of values that a point/spot could have.
 

- **CombinationsCalculator**: Just a shortcut for calculating combinations.
  - NumOfPoints:int - Number of points/spots for a value to be.
  - NumOfValues:int - Number of values that a point/spot could have.


- **GetMedian**: Returns the middle of a list, with a bool to automatically sort it for you.
  - inputList:list - The list to get the median of.
  - sortList:bool - Should python sort the list automatically?
  - IsNotOnlyNumbers:bool - If the list contains more than just numbers, set to true.
 
 
- **saveJsonToFile**: Saves a dictionary or list variable as a '.json' file.
  - file_path:str - The file's path to write/save to.
  - data - A dictionary or list to save as JSON data
 

- **getJsonFromFile**: Reads and returns a '.json' file as a dictionary or list.
  - file_path:str - The file's path to read from.

### Classes:

- **ConflictingInputsDetected**: An error class that is fired when using conflicting arguments in a function.