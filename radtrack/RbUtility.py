import math
import string

# How to use:
#
# convertUnitsNumber(5, "km", "m") returns 5000
# convertUnitsString("5 km", "m") returns "5000 m"
# convertUnitsNumberToString(5, "km", "m") returns "5000 m"
# convertUnitsStringToNumber("5 km", "m") returns 5000
# displayWithUnitsNumber(5000, "m") returns "5 km"
# displayWithUnitsString("5000 m") returns "5 km"
#
# The above functions should be used instead of __parseUnits
# or the __unitConversion dictionary
#
# __parseUnits("km") returns 1000


def __parseUnits(unit):
    # Attempt parsing of compound unit (e.g., 'm/s^2')
    convertValue = 1.0
    currentUnit = ''
    multiply = True

    for char in (unit + '*'): # add extra '*' to process last unit
        if char in ['/', '*']:
            if '^' in currentUnit:
                currentUnit, exponent = currentUnit.split('^')
                exponent = float(exponent)
            else:
                exponent = 1.0
            exponent = exponent if multiply else -exponent
            convertValue = convertValue*(__unitConversion[currentUnit]**exponent)
            multiply = (char == '*')
            currentUnit = ''
        else:
            currentUnit = currentUnit + char

    return convertValue

def separateNumberUnit(inputString):
    # How this works: after stripping all whitespace, the functions looks for
    # the largest continuous block of characters starting from the left that
    # can be converted to a float.  The rest (if any) are assumed to specify
    # the units.
    parse = removeWhitespace(inputString)

    for numLength in range(len(parse),-1,-1):
        try:
            number = float(parse[:numLength])
            unit = parse[numLength:]
            if unit.startswith('/'):
                unit = '1' + unit
                number = float(parse[:(numLength-1)])
        except ValueError:
            continue
        else:
            break

    try:
        return number, unit
    except UnboundLocalError:
        return float(inputString), ''


def convertUnitsNumber(number, oldUnit, newUnit):
    oldUnit = removeWhitespace(oldUnit)
    newUnit = removeWhitespace(newUnit)

    if '' in [oldUnit, newUnit] and '%' not in [oldUnit, newUnit]:
        return number # values without units don't get converted

    try:
        return number*__parseUnits(oldUnit)/__parseUnits(newUnit)
    except (ValueError, KeyError):
        raise ValueError('Cannot convert "' + oldUnit + '" to "' + newUnit + '".')

def convertUnitsString(inputString, newUnit):
    number, unit = separateNumberUnit(inputString)
    if not unit:
        return inputString
    return convertUnitsNumberToString(number, unit, newUnit)

def convertUnitsNumberToString(number, oldUnit, newUnit):
    return (str(convertUnitsNumber(number, oldUnit, newUnit)) + ' ' + removeWhitespace(newUnit)).strip()

def convertUnitsStringToNumber(inputString, newUnit):
    value, unit = separateNumberUnit(inputString)
    return convertUnitsNumber(value, unit, newUnit)

# This function converts a value to units that result in the
# smallest number larger than one.
def displayWithUnitsNumber(value, currentUnit):
    if currentUnit is None:
        return str(value)
    if value == 0:
        return str(value) + ' ' + currentUnit

    # Separate compound units
    # 'ft/sec' -> 'ft' '/sec'
    restUnit = ''
    for symbol in ['/', '*']:
        i = currentUnit.find(symbol)
        if i > -1:
            currentUnit, restUnit = currentUnit[:i], currentUnit[i:] + restUnit

    # Convert only first part of compound unit
    if '^' in currentUnit:
        baseUnit, exponent = currentUnit.split('^')
    else:
        baseUnit, exponent = currentUnit, None
    extra = '' if exponent is None else ('^' + exponent)
    try:
        group = unitTable[baseUnit]
        if '-' in extra: # negative exponent
            group = reversed(group)
        for unit in [u + extra for u in group]:
            newValue = convertUnitsNumber(value, currentUnit, unit)
            if newValue >= 1:
                break
        return str(newValue) + ' ' + unit + restUnit
    except KeyError:
        return str(value) + ' ' + currentUnit

def displayWithUnitsString(inputString):
    value, unit = separateNumberUnit(inputString)
    return displayWithUnitsNumber(value, unit)

# Unit Conversions
__unitConversion = dict()
__unitConversion[''] = 1 # unitless unit
__unitConversion['1'] = 1 # for inverse units (1/s = Hz)
unitTable = dict()
prefixes = ['P', 'T', 'G', 'M', 'k', '', 'm', 'u', 'n', 'p', 'f', 'a']
firstMultiplier = 1.0e15 # value of first unit prefix in prefixes
def addMetricUnit(unit, first = prefixes[0], last = prefixes[-1], addRow = True):
    multiplier = firstMultiplier
    row = []
    add = False
    for prefix in prefixes:
        if prefix == first:
            add = True
        if add:
            __unitConversion[prefix + unit] = multiplier
            row.append(prefix + unit)
        if prefix == last:
            break

        multiplier = multiplier/1000

    if addRow:
        addToUnitTable(row)

def addToUnitConversion(unit, value, otherUnit):
    __unitConversion[unit] = value*__unitConversion[otherUnit]

def addToUnitTable(row):
    for unit in row:
        unitTable[unit] = row

#percent -> fraction
addToUnitConversion('%', .01, '')
addToUnitTable(['%'])

#length units -> meters
addMetricUnit('m', 'k', 'f', False)
addToUnitConversion('cm', .01, 'm')
addToUnitConversion('micron', 1, 'um')
addToUnitConversion('ang', .1, 'nm')
addToUnitConversion('in', 2.54, 'cm')
addToUnitConversion('mil', .001, 'in')
addToUnitConversion('thou', 1, 'mil')
addToUnitConversion('ft', 12, 'in')
addToUnitConversion('yd', 3, 'ft')
addToUnitConversion('mi', 5280, 'ft')
addToUnitTable(['km', 'm', 'cm', 'mm', 'um', 'nm', 'pm', 'fm'])
addToUnitTable(['mi', 'yd', 'ft', 'in', 'mil'])

#angle units -> rad
addMetricUnit('rad', '')
addToUnitConversion('deg', math.pi/180, 'rad')

#temporal frequency -> Hz
addMetricUnit('Hz')
addToUnitConversion('1/s', 1, 'Hz')

#time -> seconds
addMetricUnit('s', '', 'f', False)
addMetricUnit('sec', '', 'f', False)
addToUnitConversion('min', 60, 'sec')
addToUnitConversion('hr', 60, 'min')
addToUnitTable(['hr', 'min', 's', 'ms', 'us', 'ns', 'ps', 'fs'])

#energy units -> eV
addMetricUnit('eV')

#charge units -> C
addMetricUnit('C')

#magnet units -> T
addMetricUnit('T')
addToUnitConversion('G', .0001, 'T')
addToUnitConversion('mG', .001, 'G')

#current -> A
addMetricUnit('A')

#energy -> J
addMetricUnit('J')

#power -> W
addMetricUnit('W')

#electrical resistance -> Ohm
addMetricUnit('Ohm')

#electrical potential -> V
addMetricUnit('V')

#mks mass -> g
addMetricUnit('g', 'k')


# Round number x to sig significant figures
def roundSigFig(x, sig):
    try:
        # find a, b such that x = a*10^b (1 <= a < 10)
        b = math.floor(math.log10(abs(x)))
        a = x/(10**b)
        return round(a, sig-1)*(10**b)
    except ValueError:
        return 0


rpnOp = dict()
# Basic Math
rpnOp['+'] = lambda stack : stack.pop(-2) + stack.pop(-1)
rpnOp['-'] = lambda stack : stack.pop(-2) - stack.pop(-1)
rpnOp['*'] = lambda stack : stack.pop(-2) * stack.pop(-1)
rpnOp['mult'] = lambda stack : rpnOp['*'](stack)
rpnOp['/'] = lambda stack : stack.pop(-2) / stack.pop(-1)
rpnOp['sqr'] = lambda stack : stack.pop(-1)**2
rpnOp['sqrt'] = lambda stack : math.sqrt(stack.pop(-1))
rpnOp['pow'] = lambda stack : stack.pop(-2)**stack.pop(-1)
rpnOp['chs'] = lambda stack : -stack.pop(-1)
rpnOp['abs'] = lambda stack : abs(stack.pop(-1))
rpnOp['mod'] = lambda stack : stack.pop(-2) % stack.pop(-1)
rpnOp['rec'] = lambda stack : 1/stack.pop(-1)
rpnOp['max2'] = lambda stack : max(stack.pop(-2), stack.pop(-1))
rpnOp['min2'] = lambda stack : min(stack.pop(-2), stack.pop(-1))
rpnOp['sign'] = lambda stack : stack.pop(-1) if stack[-1] == 0 else (1 if stack.pop(-1) > 0 else -1)

# Constants
rpnOp['pi'] = lambda stack : math.pi
rpnOp['log_10'] = lambda stack : math.log(10)
rpnOp['HUGE'] = lambda stack : math.exp(100)

# Physics Constants
rpnOp['mev'] = lambda stack : 0.51099906 # electron mass in MeV
rpnOp['c_mks'] = lambda stack : 299792458 # speed of light in mks
rpnOp['c_cgs'] = lambda stack : rpnOp['c_mks'](stack)*100 # speed of light in cm/s
rpnOp['e_cgs'] = lambda stack : 4.80325e-10 # elementary charge is cgs
rpnOp['e_mks'] = lambda stack : 1.60217733e-19 # elementary charge in mks
rpnOp['me_cgs'] = lambda stack : 9.1093897e-28 # mass of electron in cgs
rpnOp['me_mks'] = lambda stack : rpnOp['me_cgs'](stack)/1000 # mass of electron in mks
rpnOp['re_cgs'] = lambda stack : 2.81794092e-13
rpnOp['re_mks'] = lambda stack : rpnOp['re_cgs'](stack)/100
rpnOp['kb_cgs'] = lambda stack : 1.380658e-16
rpnOp['kb_mks'] = lambda stack : rpnOp['kb_cgs'](stack)/1e7
rpnOp['hbar_mks'] = lambda stack : 1.0545887e-34
rpnOp['hbar_MeVs'] = lambda stack : 6.582173e-22
rpnOp['mp_mks'] = lambda stack : 1.6726485e-27 # mass of proton in mks
rpnOp['mu_o'] = lambda stack : 4*math.pi*1e-7 # vacuum permeability
rpnOp['eps_o'] = lambda stack : 1/((rpnOp['c_mks'](stack)**2) * rpnOp['mu_o'](stack)) # vacuum permittivity
### Alpha Magnet
rpnOp['Kas'] = lambda stack : 191.655e-2
rpnOp['Kaq'] = lambda stack : 75.0499e-2

### Relativistic Functions
rpnOp['beta.p'] = lambda stack : stack[-1]/math.sqrt(1 + (stack.pop(-1)**2))
rpnOp['gamma.p'] = lambda stack : math.sqrt(1 + (stack.pop(-1)**2))
rpnOp['gamma.beta'] = lambda stack : 1/math.sqrt((stack.pop(-1)**2) - 1)
rpnOp['p.beta'] = lambda stack : stack[-1]/sqrt(1 - (stack.pop(-1)**2))
rpnOp['p.gamma'] = lambda stack : math.sqrt((stack.pop(-1)**2) - 1)

# Trigonometry
rpnOp['dasin'] = lambda stack : (180.0/math.pi)*math.asin(stack.pop(-1))
rpnOp['asin'] = lambda stack : math.asin(stack.pop(-1))
rpnOp['sin'] = lambda stack : math.sin(stack.pop(-1))
rpnOp['dsin'] = lambda stack : math.sin((math.pi/180)*stack.pop(-1))
rpnOp['dacos'] = lambda stack : (180.0/pi)*math.acos(stack.pop(-1))
rpnOp['acos'] = lambda stack : math.acos(stack.pop(-1))
rpnOp['cos'] = lambda stack : math.cos(stack.pop(-1))
rpnOp['dcos'] = lambda stack : math.cos((math.pi/180)*stack.pop(-1))
rpnOp['datan'] = lambda stack : (180.0/pi)*math.atan(stack.pop(-1))
rpnOp['atan'] = lambda stack : math.atan(stack.pop(-1))
rpnOp['tan'] = lambda stack : math.tan(stack.pop(-1))
rpnOp['dtan'] = lambda stack : math.tan((pi/180)*stack.pop(-1))
rpnOp['rtod'] = lambda stack : stack.pop(-1)*180/math.pi
rpnOp['dtor'] = lambda stack : stack.pop(-1)*math.pi/180
rpnOp['hypot'] = lambda stack : math.hypot(stack.pop(-2), stack.pop(-1))
# Usage: [x1 y1 x2 y2 dist2]
rpnOp['dist2'] = lambda stack : math.hypot(stack.pop(-4) - stack.pop(-2), stack.pop(-2) - stack.pop(-1))
rpnOp['knee'] = lambda stack : (math.atan(stack.pop(-1)) + (math.pi/2))/math.pi
rpnOp['Tn'] = lambda stack : math.cos(math.acos(stack.pop(-2))*stack.pop(-1))

# Hyperbolic Trig
rpnOp['cosh'] = lambda stack : math.cosh(stack.pop(-1))
rpnOp['acosh'] = lambda stack : math.acosh(stack.pop(-1))
rpnOp['sinh'] = lambda stack : math.sinh(stack.pop(-1))
rpnOp['asinh'] = lambda stack : math.asinh(stack.pop(-1))
rpnOp['tanh'] = lambda stack : math.tanh(stack.pop(-1))
rpnOp['atanh'] = lambda stack : math.atanh(stack.pop(-1))

# Powers and Logs
rpnOp['10x'] = lambda stack : 10**stack.pop(-1)
rpnOp['log'] = lambda stack : math.log10(stack.pop(-1))
rpnOp['ln'] = lambda stack : math.log(stack.pop(-1))

# Stack manipulation
rpnOp['='] = lambda stack : stack[-1]
rpnOp['over'] = lambda stack : stack[-2]
rpnOp['swap'] = lambda stack : stack.pop(-2)
def minmaxN(stack, wantMax):
    N = stack.pop(-1)
    lst = []
    for loop in range(N):
        lst.append(stack.pop())
    if wantMax:
        return max(lst)
    else:
        return min(lst)
rpnOp['maxN'] = lambda stack : maxN(stack, True)
rpnOp['minN'] = lambda stack : maxN(stack, False)

# Booleans
rpnOp['true'] = lambda stack : True
rpnOp['false'] = lambda stack : False
rpnOp['=='] = lambda stack : stack.pop(-2) == stack.pop(-1)
rpnOp['test'] = lambda stack : 'true' if stack.pop(-1) else 'false'

def rpn(expression):
    valueStack = []
    for token in expression.strip('"').split():
        try:
            valueStack.append(float(token))
        except ValueError: # token is not a number
            try:
                valueStack.append(rpnOp[token](valueStack))
            except (KeyError, IndexError):
                # named function not defined in rpnOp or valueStack is empty
                raise ValueError('Token: "' + token + '" in "' + expression + '" is not a valid RPN expression.')
    if len(valueStack) == 1:
        return valueStack[0]
    else:
        raise ValueError('"' + expression + '" is not a valid RPN expression.')



# Divides a string into lines of maximum width 'lineWidth'. 'endLine' specifies
# a string to be appended to any wrapped lines if a continuation character is
# needed. The variable 'indenting' specifies a number of spaces to indent the
# wrapped lines.
def wordwrap(line, lineWidth, endLine = '', indenting = 0):
    if indenting > lineWidth/2:
        indenting = lineWidth/2
    line = line.replace('\n',' ') # get rid of any existing newlines
    lineBegin = 0 # location of last line break
    newLine = endLine + '\n'
    indent = ' '*indenting

    # word wrap: maximum line length is lineWidth
    while lineBegin + lineWidth < len(line):
        # location of editing cursor
        lineEdit = lineBegin + lineWidth - len(endLine)
        while (line[lineEdit] not in string.whitespace or insideQuote(line, lineEdit)) and lineEdit > lineBegin:
            lineEdit -= 1 # backup up until whitespace is found
        if lineEdit == lineBegin:
            # whitespace not found, skip ahead to next whitespace or end of line
            while (line[lineEdit] not in string.whitespace or insideQuote(line, lineEdit)) and lineEdit < len(line):
                lineEdit += 1
            if lineEdit == len(line):
                return line
        line = line[:lineEdit] + newLine + indent + line[lineEdit:].strip()
        lineBegin = lineEdit + len(newLine)

    return line

def insideQuote(line, position):
    quoted = False
    for index in range(position + 1):
        if line[index] == '"' and not characterEscaped(line, index):
            quoted = not quoted
    return quoted


def stripComments(line, commentCharacter):
    for i in range(len(line)):
        if line[i] == commentCharacter and not insideQuote(line, i) and not characterEscaped(line, i):
            return line[:i].strip()
    return line.strip()

def characterEscaped(line, position):
    return position != 0 and line[position - 1] == '\\'

def removeWhitespace(string):
    return ''.join(string)


# Generic Exception class for file read errors
class FileParseException(Exception):
    def __init__(self, message):
        self.message = message

# Returns the data-holding widget inside layout widgets (QScrollArea, etc.)
def getRealWidget(widget):
    try:
        return getRealWidget(widget.widget())
    except AttributeError:
        return widget
