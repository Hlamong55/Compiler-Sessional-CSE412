%{
#include <stdio.h>
#include <stdlib.h>
#include "lab4.tab.h"
%}

%option noyywrap

%%

[0-9]+ {
    yylval.dval = atof(yytext);
    return DIGIT;
}

\n      return '\n';
[ \t]   ;
.       return yytext[0];

%%