grammar test;

stat: nodeid;

nodeid: 'node' NUM ;

NUM: [0-9]+ ;
WS: [\t\r\n] -> skip ;
