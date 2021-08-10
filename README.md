# ledger
Simple ledger

Run: 
`./parse.py [--name <your_name>] [--path <path_to_ledger>]`

The ledger entries must be of the form
`<names> <+/-> <amount> <date> "<transaction-description>"`
  
- If there are multiple names in <names>, the amount is divided between each name. If <your_name> is one of the <names> and the transcation direction is '+', then the <amount> is divided among everyone except you.
- '+' means you get money, and '-' means you pay.
- <amount> is the transcation amount. It can also be an expression (like, $3+$5-$10/2).
- <date> is the transcation date.
- <transcation-description> must be inside quotation marks
