# 03.1.4 È uguale
1. Il programma in Python inizia allocando una variabile `x` con un valore `float` di `3.0`.
2. Continua poi controllando se una variabile **non definita** `s` corrisponde al valore `str` di `'sette punto cinque'`.
    1. Questo controllo è inutile poiché non viene mai utilizzato.
3. Procede poi tentando di controllare se la variabile `x` di prima corrisponde al valore `float` di `3.0`.
    1. Questo controllo inizierebbe un'eccezione di tipo `SyntaxError` poiché utilizza l'operatore di assegnazione `=` anziché quello di controllo per uguaglianza, `==`.
    2. Immaginando che il codice sia corretto e che, dunque, utilizzi `==`, sarebbe inutile poiché la variabile `x` non ha la possibilità di mutare dal momento della sua assegnazione. Dunque, la condizione sarà sempre vera.
    3. Se la condizione fosse vera, il codice vorrebbe assegnare alla variabile `s` il valore `str` di `tre punto zero`. Nuovamente, però, utilizza l'operatore sbagliato, ovvero quello di uguaglianza anziché quello di assegnazione. Questo risulta in un controllo (inutile poiché non utilizzato) di uguaglianza.
4. Infine, il programma stampa sul terminale il valore della variabile `s`.