# Written by EnvyingGolem47
# 3/8/2023

# Current Version Date: 12/6/2023

import re

class ConflictingInputsDetected(Exception):
    """
    When this is raised, it is because two conflicting inputs were used in a
    custom function.

    For Example, such as when two or more bool statements are being switched on
    and are incompatible toggles.

    Another Example, an invalid input without the correct toggle was used can use this exception.
    """
    pass

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

            for i in range(1):
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
    x = 0
    for i in range(NumOfPoints+1):
        if(x==0):
            x=NumOfValues
        else:
            x = x * NumOfValues
    return x

def SanitizeString(string:str,TestFor:bool=False,PrintFound:bool=True,bannedcharacters:list=['$','&','{','}','\\','/','[',']']):
    """
    PrintFound will only matter if TestFor is set to True.

    :param string:
    :param TestFor:
    :param PrintFound:
    :param bannedcharacters:
    :return:
    """

    if(TestFor == True):

        found = []

        for i in bannedcharacters:

            if(i in string and not PrintFound):
                del found
                return True

            elif(i in string and PrintFound):
                found.append(i)

        if(found != [] and PrintFound):

            return found

        return found

    else:

        for i in bannedcharacters:
            string.replace(i,'')

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

    for i in range(1):
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