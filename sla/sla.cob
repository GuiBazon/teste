       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALCULADORA.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       77 NUM1 PIC 9(4).
       77 NUM2 PIC 9(4).
       77 RESULT PIC 9(8).
       77 OP PIC X.

       PROCEDURE DIVISION.
           DISPLAY "Digite o primeiro numero: "
           ACCEPT NUM1
           DISPLAY "Digite o segundo numero: "
           ACCEPT NUM2
           DISPLAY "Escolha a operacao (+ - * /): "
           ACCEPT OP

           IF OP = "+"
               COMPUTE RESULT = NUM1 + NUM2
           ELSE IF OP = "-"
               COMPUTE RESULT = NUM1 - NUM2
           ELSE IF OP = "*"
               COMPUTE RESULT = NUM1 * NUM2
           ELSE IF OP = "/"
               COMPUTE RESULT = NUM1 / NUM2
           ELSE
               DISPLAY "Operacao invalida."
           END-IF

           DISPLAY "Resultado: " RESULT
           STOP RUN.
