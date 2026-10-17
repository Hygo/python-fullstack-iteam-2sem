# Como obter e entregar as atividades

O repositório oficial do curso (`Hygo/python-fullstack-iteam-2sem`) é o **material do professor** e é somente para leitura. As atividades **não** são feitas nele e **não** se envia Pull Request para lá: cada aluno cria a **sua própria cópia** e trabalha nela.

> Pull Requests abertos no repositório oficial são fechados automaticamente.

## O que você precisa

- Uma conta no GitHub
- [Git](https://git-scm.com/downloads) instalado (teste com `git --version`)
- Python 3 e uma IDE (veja o Módulo 1 da apostila)

## 1. Criar a sua cópia (só uma vez)

1. Abra https://github.com/Hygo/python-fullstack-iteam-2sem
2. Clique em **Use this template** → **Create a new repository**.
3. Em *Owner*, escolha a sua conta. Em *Repository name*, use `python-fullstack-seunome`.
4. Escolha a visibilidade:
   - **Public**: mais simples, o professor acessa direto pelo link.
   - **Private**: depois, convide o usuário `Hygo` em *Settings → Collaborators*.
5. Deixe **Include all branches** desmarcado e clique em **Create repository**.

> Não use o botão *Fork*. O *Use this template* gera uma cópia independente, só sua.

## 2. Baixar a sua cópia para o computador

Troque `SEU-USUARIO` e `seunome` pelos seus dados:

```bash
git clone https://github.com/SEU-USUARIO/python-fullstack-seunome.git
cd python-fullstack-seunome
```

A partir daqui, `origin` é a **sua cópia** (onde você envia o seu trabalho).

## 3. Conectar ao repositório do professor (só uma vez)

Isso serve apenas para **baixar** os módulos novos:

```bash
git remote add professor https://github.com/Hygo/python-fullstack-iteam-2sem.git
git remote set-url --push professor DESATIVADO
git remote -v
```

A segunda linha é uma trava de segurança: com ela, `git push professor` falha, então você nunca envia nada ao repositório original por engano.

## 4. Fazer as atividades

Trabalhe dentro da pasta do módulo e salve o progresso na **sua** cópia:

```bash
git add .
git commit -m "Atividade do módulo 1 - exercícios 01 a 05"
git push origin main
```

Faça commits pequenos e frequentes. Eles mostram o seu processo, não só o resultado final.

## 5. Receber um módulo novo

Os módulos são liberados aos poucos. Quando o professor avisar que um módulo foi liberado (exemplo com `modulo-02`):

```bash
git fetch professor
git checkout professor/main -- modulo-02
git add modulo-02
git commit -m "Adiciona material do módulo 2"
git push origin main
```

O `git checkout professor/main -- pasta` copia **somente aquela pasta** do professor para a sua cópia. O que você já fez nas outras pastas não é alterado.

> Atenção: se você já tiver alterado arquivos **dentro da pasta que está baixando**, eles serão sobrescritos pela versão do professor. Faça uma cópia do seu trabalho antes.

## 6. Entregar uma atividade

1. Marque a entrega com uma tag e envie. O nome da tag é sempre `atividade-modulo-` seguido do número do módulo com dois dígitos (exemplo com o módulo 1):

   ```bash
   git tag atividade-modulo-01
   git push origin atividade-modulo-01
   ```

2. Envie ao professor o **link da sua cópia** e o **nome da tag**, pelo canal combinado com a turma.

## Dúvidas comuns

**Posso abrir um Pull Request no repositório do professor?**
Não. Ele será fechado automaticamente. A entrega é feita pelo link da sua cópia.

**O `git push` pede usuário e senha e dá erro.**
O GitHub não aceita mais a senha da conta no Git. Use o GitHub CLI (`gh auth login`) ou o Git Credential Manager, que abre o login pelo navegador.

**Errei e quero desfazer um arquivo.**
Antes de fazer commit: `git restore nome_do_arquivo.py`.
