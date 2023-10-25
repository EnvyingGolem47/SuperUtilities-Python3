# Written by EnvyingGolem47
# 3/8/2023

# Current Version Date: 10/25/2023

import re

class ConflictingInputsDetected(Exception):
    """
    When this is raised, it is because two conflicting inputs were used in a
    custom function.

    For Example, such as when two or more bool statements are being switched on
    and are incompatible toggles.
    """
    pass

def SInput(prompt:str,IsInt:bool=False,IsBool:bool=False,IsFloat:bool=False,acceptedAnswers=[],AACaseSensitive:bool=True
           ,UseRegularExpression:bool=False,RegularExpression=r'',ReturnREListOnly:bool=False,printBypass:bool=False):
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

            inp = input(prompt)

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

def PermutationCalculator(NumOfPoints:int):
    """
    simple code that allows computing the number of possible permutations
    a sequence of points can have.

    For example, 26 different points have
    403291461126605635584000000
    number of possible permutations.

    Returns int.

    :param NumOfPoints:
    :return:
    """

    x = 0
    for i in range(NumOfPoints+1):
        if(i == 0):
            x = 1
        else:
            x = x * i
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