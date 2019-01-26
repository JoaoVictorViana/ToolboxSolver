#
#Solver de Programação Linear
#
#Instituto Federal do Ceará
#Curso: Ciência da Computação
#
#@autor: João Victor Duarte Viana
#


import sys 
from pulp import *

def lines():
	print("")
	print("------------------------------------------------------------------------------------------------")
	print("")

def createProblem(name,is_max):
	lines()
	return LpProblem(name,(LpMaximize if is_max else LpMinimize))
	
def creatVariables():
	lines()
	num_variables = int(input ("Quantas variáveis irá precisar para este problema? "))
	vetor = []
		
	for count in range(num_variables):
		print(count + 1,"Variável: ")
		name_variable = input("Qual o seu nome? ")
		low_Bound = int(input("Qual seu limite minimo? "))
		up_Bound = int(input("Qual seu limite máximo? "))
		vetor.append(LpVariable(name_variable, low_Bound, up_Bound))

	return vetor
	
def creatFuncObj(variables,problem):
	lines()
	print ("Crie agora a função objetivo.")
	func = 0
	for count in range(len(variables)):
		value = float( input("Qual o coeficiente da variável " + str(variables[count]) + " ? "))
		func += value*variables[count]
	problem += func,"Total de custos"
	
def creatRestriction(variables,problem,number):
	lines()
	print("Crie a",number,"° restrição.")
	name_restriction = input("Qual o nome desta restrição? ")
	restrict = 0
	for count in range(len(variables)):
		value = float(input("Qual o coeficiente da variável " + str(variables[count]) + " ? "))
		restrict += value*variables[count]
	
	correct = False
	
	while correct == False:
		logic = input("Qual é a inequação da " + str(count) + "° restrição (" + name_restriction + ")? (>= ou <=) ")
		value_b = float(input("Qual é o valor desta restrição? "))
		if logic == ">=":
			problem += restrict >= value_b,name_restriction 
			correct = True
		elif logic == "<=":
			problem += restrict <= value_b,name_restriction 
			correct = True
		else:
			print("Opção inválida! Por favor, digite novamente.")
		
	
def writeProblem(problem,name):
	filepath = name + ".lp"
	problem.writeLP(filepath)
	
def solveProblem(problem):
	problem.solve()
	
def printStatus(problem):
	lines()
	print("Status : ", LpStatus[problem.status])
	
def optimalSolutions(problem):
	lines()
	for variable in problem.variables():
		print(variable.name,variable.varValue)
	
def optimizedObjective(problem):
	lines()
	print("Custo total :",value(problem.objective))
	
def start():
	print ("Bem vindo!")
	run = True
	while run:
		lines()

		name = input ("Qual o nome do seu problema linear? ")
		is_max = True if input ("Você quer máximizar esse problema? [y] (Caso digite outra letra, iremos inferir que você quer minimizar esse problema) ") == "y"  else False 
		
		problem = createProblem(name,is_max)
		
		variables  = creatVariables()
		
		creatFuncObj(variables,problem)
		
		lines()
		num_restricion = int(input("Quantas restrições você colocará no seu problema? "))
		for count in range(num_restricion):
			creatRestriction(variables,problem,count+1)
				
		writeProblem(problem,name)
		
		solveProblem(problem)
		
		printStatus(problem)
		
		optimalSolutions(problem)
		
		optimizedObjective(problem)
		
		lines()
		if input("Deseja resolver mais algum problema? [y] ") != "y":
			run = False 
	
	print("Obrigado e volte sempre!")
	lines()
	
start()