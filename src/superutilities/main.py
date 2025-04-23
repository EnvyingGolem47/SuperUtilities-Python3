# Written by EnvyingGolem47
# 3/8/2023

# Current Version Date: 4/21/2025

import re
import json
import datetime

class ConflictingInputsDetected(Exception):
    """
    When this is raised, it is because two conflicting inputs were used in a
    custom function.

    For Example, such as when two or more bool statements are being switched on
    and are incompatible toggles.

    Another Example, an invalid input without the correct toggle was used can use this exception.
    """
    pass

class Logger:
    def __init__(self,log_directory:str,file_date_format:str='%m-%d-%Y',timestamp_format:str='%H:%M:%S - '):
        """
        A Class to make creating and populating log files a little bit easier in python.

        The only required variable is 'log_directory', which all it needs is the directory name / path to store the log files in.

        :param log_directory:
        :param file_date_format:
        :param timestamp_format:
        """

        self.log_directory = log_directory
        self.file_date_format = file_date_format
        self.timestamp_format = timestamp_format

    def log(self,text:str,tag:str='',print_to_console:bool=True,new_line:bool=True):
        """
        Logs desired text to a log file.

        'text' is the text that is to be stored in the log file (i.e. 'Program started.")

        'tag' is an optional variable that will come before the text, it can be anything but is intended for WARN, INFO, and ERROR tags.

        If 'print_to_console' is True, then it will also use print to output it to the console.

        If 'new_line' is True, then the next log made will be on a newline.

        :param text:
        :param tag:
        :param print_to_console:
        :param new_line:
        """

        log_text = datetime.datetime.strftime(datetime.datetime.now(), "%H:%M:%S - ") + tag + text

        log_file = open(self.log_directory+datetime.datetime.strftime(datetime.datetime.now(),self.file_date_format)+'.txt','a')

        if print_to_console:
            print(log_text)

        if new_line:
            log_file.write(log_text+'\n')
        else:
            log_file.write(log_text)

        log_file.close()

def SInput(prompt:str,IsInt:bool=False,IsBool:bool=False,IsFloat:bool=False,acceptedAnswers=[],AACaseSensitive:bool=True
           ,UseRegularExpression:bool=False,RegularExpression=r'',ReturnREListOnly:bool=False
           ,printBypass:bool=False,inputBypass=None,useInputBypass:bool=False):
    """
    Similar to input() but contains its own exception handling
    As well as auto converting to the desired type.

    Cannot use IsInt, IsBool, or IsFloat together.

    Returns string or whichever type is selected.

    Accepted Answers must be in String form, even if you desire a different input type.

    AACaseSensitive, will make it so that the case must match that of the ones in Accepted Answers.

    UseRegularExpression, if set to True will use the Regular expression inserted into the Variable RegularExpression ( r'' ).

    RegularExpression takes a desired regular expression which it then compiles and uses to determine if an input is valid.

    ReturnREListOnly will bypass any other declarations including acceptedAnswers, and return what the Regular expression finds, Returns a list.

    printBypass will prevent print statements from being used, this allows the function to be used in GUI like enviroments
        With printBypass enabled, there will be two string returns besides returning a correct string:
        Invalid - Invalid input
        Cancelled - The input was cancelled (this shouldn't be possible but is here just in case)

    inputBypass is used in conjuction with printBypass to allow for full intigration with a gui.
        must toggle it with useInputBypass=True

    :param prompt:
    :param IsInt:
    :param IsBool:
    :param IsFloat:
    :param acceptedAnswers:
    :param AACaseSensitive:
    :param UseRegularExpression:
    :param RegularExpression:
    :param ReturnREListOnly:
    :param printBypass:
    :return:
    """

    while True:
        try:

            if useInputBypass == False:
                inp = input(prompt)
            else:
                inp = inputBypass

            if(UseRegularExpression and RegularExpression != r'' and re.compile(RegularExpression).findall(inp) == []):

                if(printBypass == True):
                    return "Invalid"
                else:
                    print("Invalid Input.")
                    print("Please try again.\n")
                    continue

            if (UseRegularExpression and RegularExpression != r'' and re.compile(RegularExpression).findall(inp) != [] and ReturnREListOnly):
                return re.compile(RegularExpression).findall(inp)

            if(acceptedAnswers == []):

                if(IsInt and not IsBool and not IsFloat):
                    return int(inp)

                elif(IsBool and not IsInt and not IsFloat):
                    if(inp.lower() in ['1','true','yes','y']):
                        return True
                    elif(inp.lower() in ['0','false','no','n']):
                        return False
                    else:

                        if (printBypass == True):
                            return "Invalid"
                        else:
                            print("Invalid Input.")
                            print("Please try again.\n")
                            continue

                elif(IsFloat and not IsBool and not IsInt):
                    return float(inp)

                elif(IsFloat or IsBool or IsInt):
                    raise ConflictingInputsDetected

                else:
                    return inp

            else:
                if(AACaseSensitive == False):

                    x = 0
                    for i in acceptedAnswers:

                        acceptedAnswers.pop(x)
                        acceptedAnswers.insert(x,i.lower())

                        x = x + 1

                    if (inp.lower() in acceptedAnswers):

                        if (IsInt and not IsBool and not IsFloat):
                            return int(inp)

                        elif (IsBool and not IsInt and not IsFloat):
                            if (inp.lower() in ['1', 'true', 'yes', 'y']):
                                return True
                            elif (inp.lower() in ['0', 'false', 'no', 'n']):
                                return False
                            else:

                                if (printBypass == True):
                                    return "Invalid"
                                else:
                                    print("Invalid Input.")
                                    print("Please try again.\n")
                                    continue

                        elif (IsFloat and not IsBool and not IsInt):
                            return float(inp)

                        elif (IsFloat or IsBool or IsInt):
                            raise ConflictingInputsDetected

                        else:
                            return inp

                elif(inp in acceptedAnswers and AACaseSensitive == True):

                    if (IsInt and not IsBool and not IsFloat):
                        return int(inp)

                    elif (IsBool and not IsInt and not IsFloat):
                        if (inp.lower() in ['1', 'true', 'yes', 'y']):
                            return True
                        elif (inp.lower() in ['0', 'false', 'no', 'n']):
                            return False
                        else:

                            if (printBypass == True):
                                return "Invalid"
                            else:
                                print("Invalid Input.")
                                print("Please try again.\n")
                                continue

                    elif (IsFloat and not IsBool and not IsInt):
                        return float(inp)

                    elif (IsFloat or IsBool or IsInt):
                        raise ConflictingInputsDetected

                    else:
                        return inp

                else:

                    if (printBypass == True):
                        return "Invalid"
                    else:
                        print("Invalid Input.")
                        print("Please use on of the Accepted Answers: ")
                        print(acceptedAnswers)
                        print("\n")

        except ValueError or TypeError:

            if (printBypass == True):
                return "Invalid"
            else:
                print("Invalid Input.")
                print("Please try again.\n")

        except KeyboardInterrupt:

            if (printBypass == True):
                return "Cancelled"
            else:
                print("\nSuper Input Cancelled.")

            # Using a break because of a weird behaviour where it gets put back into the loop
            # Also deleting inp, because of a weird memory behaviour
            try:
                del inp
                break
            except:
                break

def PermutationCalculator(NumOfPoints:int,NumOfValues:int):
    """
    simple code that allows computing the number of possible permutations
    a sequence of points can have.

    For example, 26 different points have
    403291461126605635584000000
    number of possible permutations.

    Returns int.

    :param NumOfPoints:
    :param: NumOFValues
    :return:
    """

    def fct(n):
        fact = 1

        for i in range(1, n+1):
            fact = fact * i

        return fact

    return fct(NumOfPoints)/fct(NumOfPoints-NumOfValues)

def CombinationsCalculator(NumOfPoints:int,NumOfValues:int):
    """
    Shortcut for remembering how to calculate possible combinations.

    :param NumOfPoints:
    :param NumOfValues:
    :return:
    """

    return NumOfValues ** NumOfPoints

def SanitizeString(string:str, TestFor:bool=False, PrintFound:bool=True,
                   bannedCharacters:list=['$', '&', '{', '}', '\\', '/', '[', ']'],
                   replaceWith:str=''):
    """
    PrintFound will only matter if TestFor is set to True.

    replaceWith will replace whatever is sanitized with that respective string. Default is nothing.

    :param string:
    :param TestFor:
    :param PrintFound:
    :param bannedCharacters:
    :param replaceWith:
    :return:
    """

    if(TestFor == True):

        found = []

        for i in bannedCharacters:

            if(i in string and not PrintFound):
                del found
                return True

            elif(i in string and PrintFound):
                found.append(i)

        if(found != [] and PrintFound):

            return found

        return found

    else:

        for i in bannedCharacters:
            
            string = string.replace(i,replaceWith)

        return string

def getMedian(inputList:list,sortList:bool=True,IsNotOnlyNumbers:bool=False):
    """
    Prints the median of the given NUMERICAL list.

    If sortList is set to false, the function will not sort it for you.

    If IsNotOnlyNumbers is set to true, it will output the middle values.

    This will return None if given an empty list.

    :param inputList:
    :param sortList:
    :param IsNotOnlyNumbers:
    :return: 
    """

    if(len(inputList) == 1):
        return inputList[0]
    elif(len(inputList) == 0):
        return None

    if(sortList == True):
        inputList.sort()

    if(IsNotOnlyNumbers == False):
        if(len(inputList) % 2 != 0):
            return inputList[int((len(inputList)/2) - .5)]
        else:
            return ((inputList[(len(inputList)//2)-1]+inputList[(len(inputList)//2)])/2)
    else:
        if(len(inputList) % 2 != 0):
            return inputList[int((len(inputList)/2) - .5)]
        else:
            return [inputList[int((len(inputList)/2) - .5)],inputList[int((len(inputList)/2) + .5)]]

def saveJsonToFile(file_path:str,data,indent:int=4):
    """
    Saves a dictionary, or a list, to a JSON file.

    Has no internal error handling.

    :param file_path:
    :param data:
    :return:
    """
    with open(file_path,'w') as file:
        json.dump(data,file,indent=indent)

    file.close()

def getJsonFromFile(file_path:str):
    """
    Reads and returns a JSON file as a dictionary, or a list.

    Has no internal error handling.

    :param file_path:
    :return:
    """
    with open(file_path, 'r') as file:
        data = json.load(file)

    file.close()
    return data