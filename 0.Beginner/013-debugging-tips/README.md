# Debugging Tips

Neste projeto foram reforçados conceito de debug, desde dicas em como fazer um debug em uma IDE, até dicas de coisas mais simples, como a utilização do print, try e except, pausar um pouco, relaxar e voltar para analisar o que pode estar gerando um bug, etc.

Com isso não houve o desenvolvimento em si, de um projeto em código, porém ainda assim foi uma aula bem importante.

Algumas dicas do uso do debugger do pycharm (em inglês):

Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging. This is normally known as the debugger. In many ways, they are like print statements on steroids.

Debuggers allows us to peek into our code during execution and pause on chosen lines to figure out what is the inner mechanism and where it's going wrong.

There are a couple of things that are the same in most IDEs which you should be familiar with:

Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). This line will be where the program pauses during debug run.

Step Over - This button will go through the execution of your code line by line and allow you to view the intermediate values of your variables.

Step Into - This will enter into any other modules that your code references. e.g. If you use a function from the random module it will show you the original code for that function so you can better understand its functionality and how it relates to your problems.