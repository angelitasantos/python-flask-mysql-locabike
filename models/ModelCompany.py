from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *
from models.Form import *


def CompanyRegister():
    form = ModelFormPeople()
    if request.method == 'POST':
        nome = form.nome.data
        razaosocial = form.razaosocial.data
        tipo = form.tipo.data
        cnpj = form.cnpj.data
        inscest = form.inscest.data
        cpf = form.cpf.data
        rg = form.rg.data
        endereco = form.endereco.data
        
        numero = form.numero.data
        complemento = form.complemento.data
        bairro = form.bairro.data
        cidade = form.cidade.data
        uf = form.uf.data
        cep = form.cep.data
        telefone1 = form.telefone1.data
        telefone2 = form.telefone2.data
        email = form.email.data

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM companies WHERE email = %s', [email])
            cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                cursor = mysql.connection.cursor()
                cursor.execute('''INSERT INTO companies 
                (nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
                bairro, cidade, uf, cep, telefone1, telefone2, email) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                [nome, razaosocial, tipo, cnpj, inscest, 
                cpf, rg, endereco, numero, complemento,
                bairro, cidade, uf, cep, telefone1, telefone2, email])
                mysql.connection.commit()
                flash('Company Created Successfully...!!!', 'success')
            else:
                flash('Company Found...!!!', 'danger')
        except Exception as error:
            print(error)


def CompanyUpdate():
    form = ModelFormPeople()
    if request.method == 'POST':
        nome = form.nome.data
        razaosocial = form.razaosocial.data
        tipo = form.tipo.data
        cnpj = form.cnpj.data
        inscest = form.inscest.data
        cpf = form.cpf.data
        rg = form.rg.data
        endereco = form.endereco.data
        
        numero = form.numero.data
        complemento = form.complemento.data
        bairro = form.bairro.data
        cidade = form.cidade.data
        uf = form.uf.data
        cep = form.cep.data
        telefone1 = form.telefone1.data
        telefone2 = form.telefone2.data
        email = form.email.data
        id = form.id.data

        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE companies 
        SET nome = %s, razaosocial = %s, tipo = %s, cnpj = %s, inscest = %s, cpf = %s, rg = %s,
        endereco = %s, numero = %s, complemento = %s, bairro = %s, cidade = %s,
        uf = %s, cep = %s, telefone1 = %s, telefone2 = %s, email = %s
        WHERE id = %s''',
        [nome, razaosocial, tipo, cnpj, inscest, 
        cpf, rg, endereco, numero, complemento,
        bairro, cidade, uf, cep, telefone1, telefone2, email, id])
        mysql.connection.commit()
        flash("Company Updated Successfully...!!!", "success")