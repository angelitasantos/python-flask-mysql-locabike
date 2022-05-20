from flask import Flask, render_template, url_for, redirect, flash, session, request, jsonify
from conexao_mysql import *
from models.Form import *


def ProviderRegister():
    form = ModelFormPeople()
    if request.method == 'POST':
        grupo = form.grupo.data.upper()
        subgrupo = form.subgrupo.data.upper()
        nome = form.nome.data.upper()
        razaosocial = form.razaosocial.data.upper()
        tipo = form.tipo.data.upper()
        cnpj = form.cnpj.data
        inscest = form.inscest.data
        cpf = form.cpf.data
        rg = form.rg.data.upper()
        endereco = form.endereco.data.upper()
        
        numero = form.numero.data.upper()
        complemento = form.complemento.data.upper()
        bairro = form.bairro.data.upper()
        cidade = form.cidade.data.upper()
        uf = form.uf.data.upper()
        cep = form.cep.data
        telefone1 = form.telefone1.data
        telefone2 = form.telefone2.data
        email = form.email.data.lower()
        id_company = form.id_company.data

        try:
            cursor = mysql.connection.cursor()
            cursor.execute('SELECT * FROM providers WHERE email = %s', [email])
            cursor.fetchone()
            cursor.close()
            count = cursor.rowcount
            if count == 0:
                cursor = mysql.connection.cursor()
                cursor.execute('''INSERT INTO providers 
                (grupo, subgrupo, nome, razaosocial, tipo, cnpj, inscest, cpf, rg, endereco, numero, complemento,
                bairro, cidade, uf, cep, telefone1, telefone2, email, id_company) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                [grupo, subgrupo, nome, razaosocial, tipo, 
                cnpj, inscest, cpf, rg, endereco, 
                numero, complemento, bairro, cidade, uf, 
                cep, telefone1, telefone2, email, id_company])
                mysql.connection.commit()
                flash('Provider Created Successfully...!!!', 'success')
            else:
                flash('Provider Found...!!!', 'danger')
        except Exception as error:
            print(error)


def ProviderUpdate():
    form = ModelFormPeople()
    if request.method == 'POST':
        grupo = form.grupo.data.upper()
        subgrupo = form.subgrupo.data.upper()
        nome = form.nome.data.upper()
        razaosocial = form.razaosocial.data.upper()
        tipo = form.tipo.data.upper()
        cnpj = form.cnpj.data
        inscest = form.inscest.data
        cpf = form.cpf.data
        rg = form.rg.data.upper()
        endereco = form.endereco.data.upper()
        
        numero = form.numero.data.upper()
        complemento = form.complemento.data.upper()
        bairro = form.bairro.data.upper()
        cidade = form.cidade.data.upper()
        uf = form.uf.data.upper()
        cep = form.cep.data
        telefone1 = form.telefone1.data
        telefone2 = form.telefone2.data
        email = form.email.data.lower()
        id = form.id.data
        id_company = form.id_company.data

        cursor = mysql.connection.cursor()
        cursor.execute('''UPDATE providers 
        SET grupo = %s, subgrupo = %s, nome = %s, razaosocial = %s, tipo = %s, cnpj = %s, inscest = %s, cpf = %s, rg = %s,
        endereco = %s, numero = %s, complemento = %s, bairro = %s, cidade = %s,
        uf = %s, cep = %s, telefone1 = %s, telefone2 = %s, email = %s, id_company = %s
        WHERE id = %s''',
        [grupo, subgrupo, nome, razaosocial, tipo, 
        cnpj, inscest, cpf, rg, endereco, 
        numero, complemento, bairro, cidade, uf, 
        cep, telefone1, telefone2, email, id_company, id])
        mysql.connection.commit()
        flash("Provider Updated Successfully...!!!", "success")