import ply.lex as lex
import ply.yacc as yacc
import re
header=[]


#https://www.worldometers.info/coronavirus/
###DEFINING TOKENS###
tokens = ('BEGINTABLE','SEARCH','CLOSESEARCH','ENDTABLE', 'OPENTABLE', 'CLOSETABLE', 'OPENROW', 'CLOSEROW','OPENHEADER', 'CLOSEHEADER', 'OPENHREF', 'CLOSEHREF','CONTENT', 'OPENDATA', 'CLOSEDATA' ,
          'OPENSPAN','CLOSESPAN', 'OPENDIV', 'CLOSEDIV', 'OPENSTYLE', 'CLOSESTYLE','GARBAGE','OPENIMAGE','OPENHEADER1', 'CLOSEHEADER1')

t_ignore = '\t'


def t_BEGINTABLE(t):
    r'<table.id="main_table_countries_yesterday".[^>]*>'
    return t

""" def t_SEARCH(t):
    r'<tr.class="total_row_world.row_continent"\s*data-continent="[a-zA-Z/ ]+"\s*style="display:\s*none">|<tr.class="row_continent.total_row".data-continent="[a-zA-Z/ ]+".style="display:\s*none">'
    return t

def t_CLOSESEARCH(t):
    r'<td.style="display:none;".data-continent="[a-zA-Z ]+">'
    return t """
def t_ENDTABLE(t):
    r'<div.class="tab-pane.".id="nav-yesterday2".role="tabpanel".aria-labelledby="nav-yesterday2-tab">'
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
    r'<th [^>]*>'
    return t

def t_CLOSEHEADER(t):
    r'</th [^>]*>'
    return t
def t_OPENHEADER1(t):
    r'<thead[^>]*>'
    return t

def t_CLOSEHEADER1(t):
    r'</thead[^>]*>'
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
    r'[A-Za-z0-9&^\+,\-\/\()]+'
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
    table : BEGINTABLE OPENHEADER datas CLOSEHEADER table
    | OPENTABLE datas CLOSETABLE
    '''

def p_datas(p):
    '''
    datas  : OPENROW handledata CLOSEROW datas 
           | empty
    '''
    global header
    if(len(p)==5):
        header.append(p[2])
    
    
def p_handledata(p):
    '''
    handledata : OPENHEADER content CLOSEHEADER handledata
    | OPENDATA content CLOSEDATA handledata
    | OPENDATA OPENHREF content CLOSEHREF CLOSEDATA  handledata
    | OPENDATA OPENSPAN content CLOSESPAN CLOSEDATA  handledata
    | OPENDATA CLOSEDATA handledata
    | empty
    '''
    
    if(len(p)==5):
        p[0]=p[2]+"|"+str(p[4])
    elif(len(p)==4):
        p[0]="-"+"|"+str(p[3])
    elif(len(p)==7):
        p[0]=p[3]+"|"+str(p[6])
    else:
        p[0]=''
   
def p_content(p):

    '''
    content : CONTENT content 
            | empty
    '''

    if len(p) == 3:
        # Handle the case when only CONTENT is present
        p[0] =str(p[1]) +" "+ str(p[2])
    else:
        p[0]=''



def p_empty(p):
    '''empty :'''
    p[0]=''

    

def p_error(p):
    print(p,"error")

def main():
    file_obj= open('worldometer.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    final_str=''
    flag=0
    flag1=1
    for tok in lexer:
        if(flag and tok.type=='CLOSETABLE'):
            flag=0
            final_str+=(tok.value+"\n")
            break
        if(tok.type=='BEGINTABLE'):
            final_str+=(tok.value+"\n")
            flag=1
        elif(flag):
            if(tok.type=='OPENROW' and "display:" in tok.value and "none" in tok.value):
                flag1=0
            if(not flag1 and tok.type=='CLOSEROW'):
                flag1=1
            elif(flag1):
                final_str+=(tok.value+"\n")
    lexer1 = lex.lex()
    lexer1.input(final_str)
    for tok in lexer1:
        print(tok)
    parser = yacc.yacc()
    parser.parse(final_str)
    global header
    head="Country|Total_cases|Active_cases|Total_Deaths|Total_Recovered|Total_Tests|Death/million|Tests/million|New_Case|New_death|New_Recovered|Continent"
    file1=open("table.txt","w")
    #file1.write(head+"\n")
    
    for i in header[1:]:
        #x=i.split('|')
        file1.write(x[1]+"|")
        file1.write(x[2]+"|")
        file1.write(x[8]+"|")
        file1.write(x[4]+"|")
        file1.write(x[6]+"|")
        file1.write(x[12]+"|")
        file1.write(x[11]+"|")
        file1.write(x[13]+"|")
        file1.write(x[3]+"|")
        file1.write(x[5]+"|")
        file1.write(x[7]+"|")
        file1.write(x[15]+"\n")
    file1.close()
    file_obj.close()


if __name__ == '__main__':
    main()
