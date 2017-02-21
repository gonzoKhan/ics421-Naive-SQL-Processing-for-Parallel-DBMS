grammar csvfile;

column: STRING
      | STUFF
      |
      ;

quoted_stuff: (STUFF | COMMA)+ ;

row: column (COMMA column)* NEWLINE;

rows: (row)+ ;

COMMA: ',' ;
STUFF: ~[,\n\r"]+ ;
STRING: QUOTE ~[\n\r"]* QUOTE ;
QUOTE: '"' ;
NEWLINE: ('\r')* ('\n') ;
