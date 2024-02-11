import ply.lex as lex
import ply.yacc as yacc
import re
###DEFINING TOKENS###
tokens = ('BEGINTABLE','SEARCH','CLOSESEARCH','ENDTABLE', 'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW','OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF','CONTENT', 'OPENDATA', 'CLOSEDATA' ,
          'OPENSPAN','CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE','OPENIMAGE')

t_ignore = '\t'

def t_BEGINTABLE(t):
     r'<div.class="tab-pane."\s*id="nav-yesterday"\s*role="tabpanel"\s*aria-labelledby="nav-yesterday-tab">'
     return t

def t_SEARCH(t):
    r'<tr.class="total_row_world.row_continent"\s*data-continent="[a-zA-Z/ ]+"\s*style="display:\s*none">'
    return t

def t_CLOSESEARCH(t):
    r'<td.style="display:none;".data-continent="[a-zA-Z ]+">'
    return t
def t_ENDTABLE(t):
    r'<div.class="tab-pane ".id="nav-yesterday2".role="tabpanel".aria-labelledby="nav-yesterday2-tab">'
    return t
def t_OPENTABLE(t):
    r'<tbody[^>]*>'
    return t

def t_CLOSETABLE(t):
    r'</tbody[^>]*>'
    return t

def t_OPENROW(t):
    r'<tr[^>]*>'
    return t

def t_CLOSEROW(t):
    r'</tr[^>]*>'
    return t

def t_OPENHEADER(t):
    r'<th[^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</th[^>]*>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_OPENDATA(t):
    r'<td[^>]*>'
    return t

def t_CLOSEDATA(t):
    r'</td[^>]*>'
    return t

def t_OPENDIV(t):
    r'<div[^>]*>'
    return t

def t_CLOSEDIV(t):
    r'</div[^>]*>'
    return t

def t_OPENSTYLE(t):
    r'<style[^>]*>'
    return t

def t_CLOSESTYLE(t):
    r'</style[^>]*>'
    return t
 
def t_OPENSPAN(t):
    r'<span[^>]*>'
    return t
def t_CLOSESPAN(t):
    r'</span[^>]*>'
    return t
def t_GARBAGE(t):
    r'<[^>]*>' 
    
def t_OPENIMAGE(t):
    r'<img[^>]*/>'
    return t
def t_CONTENT(t):
    r'[A-Za-z0-9,\-\/\()&. ]+'
    return t

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES

def p_start(p):
    '''start : table'''
    p[0]=p[1]

def p_table(p):
    ''' 
    table : BEGINTABLE skiptag SEARCH data table 
            | SEARCH data CLOSESEARCH table
            | ENDTABLE
    '''
    p[0]=p[1]

def p_datas(p):
    '''
    data  : OPENDATA content CLOSEDATA data 
           | CONTENT data
           | empty          
    '''
    if len(p)==5:
        print(p[2])
def p_content(p):
    '''
    content : CONTENT content
        | empty
    '''
    print(p[1])
    p[0]=p[1]
    
def p_skiptag(p):
    '''
    skiptag : CONTENT skiptag 
            | OPENDIV skiptag 
            | OPENHEADER skiptag
            | OPENROW skiptag 
            | CLOSEHEADER skiptag
            | CLOSEDIV skiptag
            | CLOSEROW skiptag
            | empty
            '''
    p[0]=p[1]

def p_empty(p):
    '''empty :'''
    p[0]=''
    pass

def p_error(p):
    pass

def main():
    file_obj= open('worldometer.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    with open ("worldometer.txt",'w',encoding='utf-8') as a:
        for tok in lexer:
            #print(tok)
            a.write(str(tok)+'\n')
    a.close()
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()

if __name__ == '__main__':
    main()