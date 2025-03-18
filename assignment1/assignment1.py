# Write your code here.
# Test 1
def hello():
    return "Hello!"

print(hello())

# Test 2
def greet(name):
    return f"Hello, {name}!"

print(greet("Alena"))

# Test 3
def calc(a, b, operation = "multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc(4, 2, "add"))
print(calc(4, 2, "subtract"))
print(calc(4, 2, "multiply"))
print(calc(4, 2, "divide"))
print(calc(4, 2, "modulo"))
print(calc(4, 2, "int_divide"))
print(calc(4, 2, "power"))
print(calc(4, 0, "divide"))
print(calc("a", 2, "multiply"))

# Test 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return f"Invalid data type: {data_type}"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."
    
print(data_type_conversion("123", "int"))
print(data_type_conversion("123.45", "float"))
print(data_type_conversion(123, "str"))
print(data_type_conversion("hi", "int"))
print(data_type_conversion("nonsense", "float"))
print(data_type_conversion(456, "bool"))

# Test 5
def grade(*args):
    try:
        if not all(isinstance(i, (int, float)) for i in args):
            return "Invalid data was provided."
        average = sum(args) / len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >=60:
            return "D"
        else:
            return "F"
    except ZeroDivisionError:
        return "Invalid data was provided."

print(grade(95, 95, 90))
print(grade(70, 75, 80))
print(grade(65, 55, 60))
print(grade(50, 40, 45))
print(grade(100, "hello", 90))
print(grade())

# Test 6
def repeat(str, count):
    result = ""
    for _ in range(count):
        result += str
    return result

print(repeat("hello", 3))
print(repeat("Good", 5))
print(repeat("repeat", 2))

# Test 7
def student_scores(option, **kwargs):
    if not kwargs:
        return "No student scores provided."
    if option == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    elif option == "mean":
        average_score = sum(kwargs.values()) / len(kwargs)
        return average_score
    
    return "Invalid option provided."

print(student_scores("best", Alena=95, Dmitrii=98, Natalia=96, Petr=90, Olga=80))
print(student_scores("mean", Alena=95, Dmitrii=98, Natalia=96, Petr=90, Olga=80))
print(student_scores("best", Alena=97, Dmitrii=98))
print(student_scores("mean", Alena=98, Natalia=97, Denis=87))
print(student_scores("unknown", Alena=100, Dmitrii=98))

# Test 8
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word.lower() not in little_words:
            words[i] = word.capitalize()

    return " ".join(words)

print(titleize("i like the oranges and the apples"))
print(titleize("i spend a lot of time at home"))

# Test 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result +="_"
    return result

print(hangman("alphabet", "ab"))
print(hangman("python", "by"))

# Test 10
def pig_latin(sentence):
    words = sentence.split()
    vowels = "aeiou"
    pig_latin_words = []

    for word in words:

        if  word.startswith("qu"):
            new_word = word[2:] + "quay"
        elif word[0] in vowels:
            new_word = word + "ay"
        else:
            consonant_cluster = ""
            for i, char in enumerate(word):
                if char in vowels:
                    break
                if word[i:i+2] == "qu":
                    consonant_cluster += "qu"
                    break
                consonant_cluster += char
            new_word = word[len(consonant_cluster):] + consonant_cluster + "ay"

        pig_latin_words.append(new_word)
    return " ".join(pig_latin_words)

print(pig_latin("hello world"))
print(pig_latin("apple orange"))
print(pig_latin("string queen"))
print(pig_latin("quick brown fox"))

