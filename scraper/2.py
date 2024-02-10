import ply.lex as lex
import ply.yacc as yacc


global previous
###DEFINING TOKENS###
tokens = ('BEGINTABLE', 'XAXIS','STARTCHART', 'HIGHCHART', 'CATEGORIES',
'CONTENT','OPENSCRIPT', 'CLOSESCRIPT', 'YAXIS', 'SERIES', 
'RESPONSIVE', 'DATA')
t_ignore = '\t'

###############Tokenizer Rules################
def t_BEGINTABLE(t):
     r"<a.href=\"/coronavirus/about/\"><strong>Learn.more.about.Worldometer\'s.COVID-19.data</strong></a>"
     return t
# t_XAXIS = r'        xAxis:'

def t_OPENSCRIPT(t):
    r'<script.type="text/javascript"[^>]*>'
    return t

def t_CLOSESCRIPT(t):
    r'</script[^>]*>'
    return t

def t_XAXIS(t):
    r'\s+xAxis:+\s{'
    return t

def t_YAXIS(t):
    r'\s+yAxis:+\s{'
    return t

def t_HIGHCHART(t):
    r'\s+Highcharts\.chart\([^{}]*\{'
    return t

def t_CATEGORIES(t):
    r'\s+categories\:'
    return t

def t_SERIES(t):
    r'\s+series\:+\s[^{]'
    return t

def t_DATA(t):
    r'\s+data\:'
    return t

def t_RESPONSIVE(t):
    r'\s+responsive\:'
    return t
# def t_OPENTABLE(t):
#     r'<tbody[^>]*>'
#     return t

# def t_CLOSETABLE(t):
#     r'</tbody[^>]*>'
#     return t

# def t_OPENROW(t):
#     r'<tr[^>]*>'
#     return t

# def t_CLOSEROW(t):
#     r'</tr[^>]*>'
#     return t

# def t_OPENHEADER(t):
#     r'<th[^>]*>'
#     return t

# def t_CLOSEHEADER(t):
#     r'</th[^>]*>'
#     return t

# def t_OPENDATA(t):
#     r'<td[^>]*>'
#     return t

# def t_CLOSEDATA(t):
#     r'</td[^>]*>'
#     return t

def t_CONTENT(t):
    r'[A-Za-z0-9\,\"\-\.\:\{\}\[\]\'\(\)  ]+'
    return t

# def t_OPENDIV(t):
#     r'<div[^>]*>'

# def t_CLOSEDIV(t):
#     r'</div[^>]*>'

# def t_OPENSTYLE(t):
#     r'<style[^>]*>'

# def t_CLOSESTYLE(t):
#     r'</style[^>]*>'

# def t_OPENSPAN(t):
#     r'<span[^>]*>'

# def t_CLOSESPAN(t):
#     r'</span[^>]*>'

# def t_GARBAGE(t):
#     r'<[^>]*>'

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_date(p):
    '''date : OPENSCRIPT HIGHCHART content XAXIS CATEGORIES content date
    | YAXIS content date
    |  HIGHCHART content XAXIS CATEGORIES content date
    | SERIES content  DATA content date
    | DATA content date
    | RESPONSIVE content date
    | CLOSESCRIPT
    '''
    if len(p)==8 and "Active Cases" in p[3]:
        print("ACTIVE CASES")
        #print(p[6].split('[')[1].split(']')[0])
    elif len(p)==6 and  "Currently Infected" in p[2]:
        print("ACTIVE CASES") #print(p[4].split('[')[1].split(']')[0])
    if len(p)==8 and "Daily Deaths" in p[3] :
        print("DAILY DEATH")
        #print(p[3],"babe",p[6])
    elif len(p)==6 and "Daily Deaths" in p[2]:
        #print(p[4].split('[')[1].split(']')[0])
        print("DAILY DEATH")
    if len(p)==8 and "Number of newly infected vs. number of recovered and discharged patients each day" in p[3]:
        print("new Recover")
    elif len(p)==6 and "New Recoveries" in p[2]:
        #print(p[4].split('[')[1].split(']')[0])
        print(p[4])


def p_skiptag(p):
    '''skiptag : CONTENT skiptag
               | empty'''

def p_script(p):
    '''script : OPENSCRIPT CONTENT HIGHCHART CLOSESCRIPT
    | empty'''
    if len(p)>10:
        print(p)
# def p_handleheader(p):
#     '''handleheader : OPENHEADER CONTENT CLOSEHEADER handleheader
#                     | empty'''
#     #if len(p) == 5:
#     #    print("Header: ", p[2])

# def p_dataCell(p):
#     '''dataCell : OPENDATA OPENHREF CONTENT CLOSEHREF CLOSEDATA dataCell
#     		| OPENDATA CONTENT OPENHREF CONTENT CLOSEHREF CLOSEDATA dataCell
#                 | OPENDATA CONTENT CLOSEDATA dataCell
#                 | OPENDATA CLOSEDATA dataCell
#                 | '''
#     if len(p) == 7:
#         print("City: ", p[3])
#     if len(p) == 8:
#         print("Team: ", p[4])

# def p_handlerow(p):
#     '''handlerow : OPENROW handleheader CLOSEROW handlerow 
#                  | OPENROW dataCell CLOSEROW handlerow
#                  | empty'''

# def p_table(p):
#     '''table : BEGINTABLE skiptag OPENTABLE handlerow '''

def p_empty(p):
    '''empty :'''
    pass

def p_content(p):
    '''content : CONTENT content
               | empty'''
    if len(p)==3:
        p[0] = p[1]+p[2]
    else:
        p[0]=''
    


def p_error(p):
    pass#print("eror",p)

#########DRIVER FUNCTION#######
def main():
    file_obj= open('iran.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
       print(tok)
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()

if __name__ == '__main__':
    main()