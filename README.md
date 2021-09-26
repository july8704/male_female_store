# male_female_store
This is my first hobby project, the general task is to prepare a data from a txt and xlsx sources to a analysis and visualization process

EL --> THE STORE MEN AND WOMEN



This is my first hobby project and it is about the sales movement of a store. This company have signed a contract we you as a data analyst freelancer and in a limited time you have to build some reports and dashboard based on a data the company gave you. The good thing is that you are free to use any tools and methodology that you want. 

"The Store Men and Women" give the next files:

Ventas.txt --> Sales from 2011 to 2014.
Abastecimiento.txt --> Supply Control, it indicates when to order an order from the supplier.
Inventario.txt --> Stock of products.
Productos.txt --> List of products and information about them.
Proveedores.xlsx --> List of company's supplier.
It is required to create a system that generates reports and dashboard considering, but first it is necessary to extract and prepare them for an analysis.

I am going to follow the next methodology.

In this hobby project I am going to do first step Extract and Load, to do that I'll use python (numpy and pandas library). I will read, prepare, verify and load the data.
Let's do it:

After a quick review of the files I conclude that the data has extra white spaces and some data are mixed in one column. For example:

The Ventas.txt files has extra white spaces between columns and the column Name contain the name and the size of the product, it happens also in the Productos.txt file. Additionally, the Abastecimiento.txt and Inventario.txt files don't have mixed data, but white spaces. Finally the Proveedores.xlsx files, as you can see it is an excel files and fortunately it does not have extract white space or mixed values.

Now, I start to use python as a programming language and github as a control version system VCS, you can follow the code here.

We are going to analyses the function read_product(): Here I go line per line deleting extract spaces (if letter == ' ' and letter_ant == ' ':) after that put a separator (";") between columns and finally I use split(';') to convert each line of the file into a list() and add to the final dataset of products. 

1st Part
def read_product ():

    x = 0

    with open("Data/Productos.txt", "r") as archivo:

        headers_producto = ""

        rows_producto = list()

        for linea in archivo:

            linea = linea.strip()

            if x == 0:

                headers_producto = linea.split()

            else:

                letter_ant = ""

                delimiter = False

                row = ""

                for letter in linea:

                    if letter == ' ' and letter_ant == ' ':

                        if delimiter == False:

                            row = row + ";"

                        delimiter = True

                        # row.append(rows)

                    else:

                        row = row + letter

                        delimiter = False

                    letter_ant = letter

                if len(row.strip().split(';')) == 5:

                    rows = row.strip().split(';')

                    rows.pop(4)

                    rows_producto.append(rows)

                else:

                    rows_producto.append(row.strip().split(';'))



            x = 1 + x


Now, we need to add a new column based on the ProductModel. This new column classify the register in 5 five categories Mountain, Road, Touring, Classic and No Clasificated.

2nd Part
clasification_column = list()
    for i in productos_df['ProductModel']:
        if str(i).find("Mountain") != -1:
            clasification_column.append('Mountain')
        elif str(i).find("Road") != -1:
            clasification_column.append('Road')
        elif str(i).find("Touring") != -1:
            clasification_column.append('Touring')
        elif str(i).find("Classic") != -1:
            clasification_column.append('Classic')
        else:
            clasification_column.append('No clasificated')

    productos_df['Clasification'] = clasification_column
    productos_df.to_csv("Data/Productos.csv", sep=";", index=True, index_label="Cons")


At the end of this step, I will get the next six files ventas.csv, inventario.csv, abastecimiento.csv, proveedores.csv and productos.csv. 
