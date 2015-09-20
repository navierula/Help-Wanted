#!/usr/bin/python
import MySQLdb
import _mysql_exceptions as me

# Obtains the person's ID from the 'people' table
# by asking for the person's first name and last name.
def getPersonID():
        
        cur = db.cursor()

        firstname = raw_input("What is the person's first name? ")
        print ""
        lastname = raw_input("What is the person's last name?  ")
        print ""

        sql = """SELECT id
        FROM people
        WHERE firstname = %s AND lastname = %s"""

        cur.execute(sql, (firstname, lastname))

        id = cur.fetchall()

        if(len(id) == 0):
                print """Please try again! There does not exist a person with that
                         first name or last name."""
                return 0
        
        elif(len(id) > 1):
                location = raw_input("What is the location of the person? ")

                sql = """SELECT id
                         FROM people
                         WHERE firstname = %s AND lastname = %s AND location=%s"""

                cur.execute(sql, (firstname, lastname,location))
                
                id = cur.fetchall()

                if(len(id) == 0):
                        print """Please try again! There does not exist a person with that
                                 first name or last name or location."""
                        return 0
                else:
                        return id[0][0]

        else:
                return id[0][0]
        
# Obtains the power's ID from the 'power' table
# by asking for the name of the power

def getPowerID():
        
        cur = db.cursor()

        name = raw_input("What is the name of the power? ")
        print ""

        sql = """SELECT pid
                 FROM power
                 WHERE name = %s"""

        cur.execute(sql, (name,))

        pid = cur.fetchall()

        if(len(pid) == 0):
                print "Please try again! There does not exist a power with that name."
                return 0

        else:
                return pid[0][0]
        
# Obtains the crime's ID from the 'crime' table
# by asking for the name of the crime

def getCrimeID():
        cur = db.cursor()

        location = raw_input("What is the location of the crime? ")
        print ""

        datetime = raw_input("What is the date of the crime? ")
        print ""

        sql = """SELECT cid
                 FROM crime
                 WHERE location = %s AND DATE(datetime) = %s"""

        try:
                cur.execute(sql, (location, datetime))
                cid = cur.fetchall()
                if(len(cid) == 0):
                        print "There does not exist a crime associated with that location or date/time."
                        return 0
                else:
                        return cid[0][0]
        except (me.OperationalError,me.DataError):
                print "We were unable to retrieve this crime."
                return 0
        
# Obtains the superhero's ID from the 'superhero' table
# by asking for the name of the superhero

def getSuperheroID():
        cur = db.cursor()

        name = raw_input("What is the name of the superhero? ")
        print ""

        sql = """SELECT sid
                 FROM superhero
                 WHERE name = %s"""

        cur.execute(sql, (name, ))
        sid = cur.fetchall()
        if(len(sid) == 0):
                print "There does not exist a superhero with that name."
                return 0
        else:
                return sid[0][0]
        
# Obtains the archenemy's ID from the 'archenemy' table
# by asking for the name of the archenemy

def getArchenemyID():

        cur = db.cursor()

        name = raw_input("What is the name of the archenemy? ")
        print ""

        sql = "SELECT aid FROM archenemy WHERE name = %s"


        cur.execute(sql, (name, ))
        aid = cur.fetchall()
        if(len(aid) == 0):
                print "There does not exist a archenemy with that name."
                return 0
        else:
                return aid[0][0]
        sp
# Displays all records in 'people'
               
def printPeople():

    cur = db.cursor() 

    cur.execute("SELECT * from people")

    for row in list(cur.fetchall()):
        print "First Name: " +str((row[1]))
        print "Last Name: " + str((row[2]))
        print "Gender: " + str((row[3]))
        print "Location: " + str((row[4]))
        print "Date of Birth: " + str((row[5]))
        print ""


# Displays all records in 'superhero'       

def printSuperhero():
        
    cur = db.cursor() 

    cur.execute("SELECT * from superhero")

    for row in list(cur.fetchall()) :
        print "Superhero Name: " +str((row[2]))
        print "Contact Info: " + str((row[3]))
        print ""
        
# Displays all records in 'archenemy'

def printArchenemy():
        
    cur = db.cursor() 

    cur.execute("SELECT * from archenemy")

    for row in list(cur.fetchall()) :
        print "Archenemy Name: " +str((row[2]))
        print "Contact Info: " + str((row[3]))
        print ""
        
# Displays all records in 'power'

def printPower():

    cur = db.cursor() 

    cur.execute("SELECT * from power")

    for row in list(cur.fetchall()) :
        print "Power Name: " +str((row[1]))
        print "Fatal?: " + str((row[2]))
        print "Description: " + str((row[3]))
        print ""
        
# Display all records in 'crime'

def printCrime():

    cur = db.cursor() 

    cur.execute("SELECT * from crime")

    for row in list(cur.fetchall()) :
        print "Location: " +str((row[1]))
        print "Date & Time: " + str((row[2]))
        print "Description: " + str((row[3]))
        print "Resolved?: " + str((row[4]))
        print ""
        
# Displays all interactions between superheroes and archenemies

def printInteraction():

    cur = db.cursor()

    sql = """SELECT superhero.name, archenemy.name
             FROM superhero, archenemy, fights
             WHERE fights.sid = superhero.sid and fights.aid = archenemy.aid"""

    cur.execute(sql)

    for row in list(cur.fetchall()):
        print "Superhero Name: " + str((row[0]))
        print "Archenemy Name: " + str((row[1]))
        print ""

# Displays all interactions between a specific superhero and all his/her archenemies

def printInteractionSup():

    cur = db.cursor()

    sid = getSuperheroID()

    sql = """SELECT superhero.name, archenemy.name
             FROM superhero, archenemy, fights
             WHERE fights.sid = %s AND fights.sid = superhero.sid AND
                 fights.aid = archenemy.aid"""

    cur.execute(sql, (sid,))

    for row in list(cur.fetchall()):
        print "Superhero Name: " +str((row[0]))
        print "Archenemy Name: " + str((row[1]))
        print ""

# Display all interactions between a specific archenemy and all his/her associated superheroes

def printInteractionArch():

    cur = db.cursor()

    aid = getArchenemyID()

    sql = """SELECT archenemy.name, superhero.name
             FROM superhero, archenemy, fights
             WHERE fights.aid = %s AND fights.sid = superhero.sid AND
             fights.aid = archenemy.aid"""

    cur.execute(sql, (aid,))

    for row in list(cur.fetchall()):
        print "Archenemy Name: " +str((row[0]))
        print "Superhero Name: " + str((row[1]))
        print ""

# Displays all superheroes and their powers

def printSuperpower():

    cur = db.cursor()

    sql = """SELECT superhero.name, power.name
             FROM superhero, power, superpower
             WHERE superpower.sid = superhero.sid AND superpower.pid = power.pid"""

    cur.execute(sql)

    for row in list(cur.fetchall()):
        print "Superhero Name: " +str((row[0]))
        print "Power Name: " + str((row[1]))
        print ""

# Display all superheroes that possess a specific power

def printAllPowerSup():

    cur = db.cursor()

    pid = getPowerID()

    sql = """SELECT superhero.name, power.name
             FROM superhero, power, superpower
             WHERE superpower.pid = %s AND superpower.sid = superhero.sid AND
             superpower.pid = power.pid"""

    cur.execute(sql, (pid,))

    for row in list(cur.fetchall()):
        print "Power Name: " +str((row[1]))
        print "Superhero Name: " + str((row[0]))
        print""

# Display all powers that a specific superhero possesses

def printAllSupPower():

    cur = db.cursor()

    sid = getSuperheroID()

    sql = """SELECT superhero.name, power.name
             FROM superhero, power, superpower
             WHERE superpower.sid = %s AND superpower.sid = superhero.sid AND
             superpower.pid = power.pid"""

    cur.execute(sql, (sid,))

    for row in list(cur.fetchall()):
        print "Superhero Name: " +str((row[0]))
        print "Power Name: " + str((row[1]))
        print ""

# Displays all archenemies and their powers

def printArchpower():

    cur = db.cursor()

    sql = """SELECT archenemy.name, power.name
             FROM archenemy, power, archpower
             WHERE archpower.aid = archenemy.aid AND archpower.pid = power.pid"""

    cur.execute(sql)

    for row in list(cur.fetchall()):
        print "Archenemy Name: " +str((row[0]))
        print "Power Name: " + str((row[1]))
        print ""

# Display all powers a specific archenemy possesses

def printAllPowerArch():

    cur = db.cursor()

    pid = getPowerID()

    sql = """SELECT archenemy.name, power.name
             FROM archenemy, power, archpower
             WHERE power.pid = %s AND archpower.aid = archenemy.aid AND
             archpower.pid = power.pid"""

    cur.execute(sql, (pid,))

    for row in list(cur.fetchall()):
        print "Power Name: " + str((row[1]))
        print "Archenemy Name: " + str((row[0]))
        print""

# Display all archenemies with a specific power

def printAllArchPower():

    cur = db.cursor()

    aid = getArchenemyID()

    sql = """SELECT archenemy.name, power.name
             FROM archenemy, power, archpower
             WHERE archenemy.aid = %s AND archpower.aid = archenemy.aid AND
             archpower.pid = power.pid"""

    cur.execute(sql, (aid,))

    for row in list(cur.fetchall()):
        print "Archenemy Name: " +str((row[0]))
        print "Power Name: " + str((row[1]))
        print""

# Displays all superheroes and the description of the crime
# they were involved in saving

def printSupersave():

    cur = db.cursor()

    sql = """SELECT superhero.name, crime.description
             FROM superhero, crime, supersave
             WHERE supersave.sid = superhero.sid AND crime.cid = supersave.cid"""

    cur.execute(sql)

    for row in list(cur.fetchall()):
        print "Superhero Name: " +str((row[0]))
        print "Crime Info: " + str((row[1]))
        print""

# Displays a specific superhero and the crime they were involved in saving

def printSupersaveSup():

    cur = db.cursor()

    sid = getSuperheroID()

    sql = """SELECT superhero.name, crime.description
             FROM superhero, crime, supersave
             WHERE supersave.sid = superhero.sid AND crime.cid = supersave.cid
             AND supersave.sid = %s"""

    cur.execute(sql, (sid,))

    for row in list(cur.fetchall()):
        print "Superhero Name: " +str((row[0]))
        print "Crime Info: " + str((row[1]))
        print ""

# Displays all archenemies and the description of the crime
# they were involved in committing

def printArchcommit():

    cur = db.cursor()

    sql = """SELECT archenemy.name, crime.description
             FROM archenemy, crime, archcommit
             WHERE archcommit.aid = archenemy.aid AND crime.cid = archcommit.cid"""

    cur.execute(sql)

    for row in list(cur.fetchall()):
        print "Archenemy Name: " +str((row[0]))
        print "Crime Info: " + str((row[1]))
        print ""

# Displays a specific archenemy and the crime they are involved in committing

def printArchcommitArch():

    cur = db.cursor()

    aid = getArchenemyID()

    sql = """SELECT archenemy.name, crime.description
             FROM archenemy, crime, archcommit
             WHERE archenemy.aid = archcommit.aid AND crime.cid = archcommit.cid
             AND archcommit.aid = %s"""

    cur.execute(sql, (aid,))

    for row in list(cur.fetchall()):
        print "Archenemy Name: " +str((row[0]))
        print "Crime Info: " + str((row[1]))
        print ""

# Displays all powers used in all crimes

def printStrategy():

    cur = db.cursor()

    sql = """SELECT power.name, crime.description
             FROM power, crime, strategy
             WHERE power.pid = strategy.pid AND crime.cid = strategy.cid"""

    cur.execute(sql)

    for row in list(cur.fetchall()):
        print "Power Name: " +str((row[0]))
        print "Crime Info: " + str((row[1]))
        print ""

# Displays all crimes associated with a specific power

def printStrategyPow():

    cur = db.cursor()

    pid = getPowerID()

    sql = """SELECT power.name, crime.description
             FROM power, crime, strategy
             WHERE power.pid = strategy.pid AND crime.cid = strategy.cid
             AND power.pid = %s"""

    cur.execute(sql,(pid,))

    for row in list(cur.fetchall()):
        print "Power Name: " +str((row[0]))
        print "Crime Info: " + str((row[1]))
        print ""

        
# Insert a record into 'people'

def insertPeople():

    cur = db.cursor() 

    firstname = raw_input("What is the person's first name? ")

    lastname = raw_input("What is the person's last name? ")

    gender = raw_input("What is the person's gender? ")

    location = raw_input("What is the person's location? ")

    dob = raw_input("What is the person's date of birth (YYYY-MM-DD)? ")

    sql = """insert into people (firstname, lastname, gender, location, dob)
                 values (%s,%s,%s,%s,%s)"""

    try:
        cur.execute(sql, (firstname, lastname, gender, location, dob))
    except (me.OperationalError,me.DataError):
        print ""
        print "This person was unable to be inserted into the database."
        return
    print ""
    print "This person has been inserted into the database."
    db.commit()

# Insert a record into 'superhero'

def insertSuperhero():

    cur = db.cursor() 

    print "First, you must enter the name of the person:"
    print ""
    
    personID = getPersonID()

    print "Now, you may enter information pertaining to the superhero:"
    print""
    
    name = raw_input("What is the person's superhero name? ")
    print ""
    contact = raw_input("What is this superhero's contact info? ")

    sql = "insert into superhero (id, name, contact) values (%s,%s,%s)"

    try:
        cur.execute(sql, (personID, name, contact))
    except (me.OperationalError,me.DataError,me.IntegrityError):
        print ""
        print "This superhero was unable to be inserted into the database."
        return

    print ""
    print "This superhero was able to be inserted into the database."
    db.commit()

# Insert a record into 'archenemy'

def insertArchenemy():

    cur = db.cursor()

    print "First, you must enter the name of the person:"
    print ""
        
    personID = getPersonID()

    print "Now, you may enter information pertaining to the archenemy:"
    print""
        
    name = raw_input("What is the archenemy's name? ")
    print ""
    contact = raw_input("What is this archenemy's contact info? ")

    sql = "insert into archenemy (id, name, contact) values (%s,%s,%s)"

    try:
        cur.execute(sql, (personID, name, contact))
    except (me.OperationalError,me.DataError,me.IntegrityError):
        print ""
        print "This archenemy was unable to be inserted into the database."
        return

    print "This archenemy was unable to be inserted into the database."
    db.commit()

# Insert a record into 'power'

def insertPower():

    cur = db.cursor() 

    name = raw_input("What is the name of the power? ")
    print ""
    fatality = raw_input("Is this power fatal (Y/N)? ")
    print ""
    description = raw_input("Enter a description of the power: ")

    sql = "insert into power (name, fatality, description) values (%s,%s,%s)"

    try:
        cur.execute(sql, (name, fatality, description))
    except (me.OperationalError,me.DataError,me.IntegrityError):
        print ""
        print "The power was unable to be inserted into the database."
        return
    print ""
    print "The power was able to be inserted into the database."
    db.commit()

# Insert a record into 'crime'

def insertCrime():

        cur = db.cursor() 

        location = raw_input("What is the location of the crime? ")
        print ""
        datetime = raw_input("When did the crime occur (YYY-MM-DD HH:MM:SS)? ")
        print ""
        description = raw_input("Describe activities involved in the crime: ")
        print ""
        resolved = raw_input("Is the crime resolved (Y/N)? ")

        sql = "insert into crime (location, datetime, description, resolved) values (%s,%s,%s,%s)"

        try:
                cur.execute(sql, (location, datetime, description, resolved))
        except (me.OperationalError,me.DataError,me.IntegrityError):
                print ""
                print "The crime was unable to be inserted into the database."
                return
        print ""
        print "The crime was able to be inserted into the database."
        db.commit()

# Insert a record into 'fights'
# superhero vs. archenemy

def insertInteraction():

        print "First, you must enter the name of the superhero and the"
        print "name of the archenemy."
        print ""

        sid = getSuperheroID()

        aid = getArchenemyID()

        cur = db.cursor()

        sql = "INSERT INTO fights VALUES (%s, %s)"

        try:
                cur.execute(sql, (sid, aid))
        except (me.OperationalError,me.DataError,me.IntegrityError):
                print ""
                print "This interaction was unable to be inserted into the database."
                return
        
        print ""
        print "This interaction was able to be inserted into the database."
        db.commit()

# Insert a record into 'supersave'
# superhero & crime

def insertSupersave():

        print "First, you must enter the name of the superhero and the"
        print "location, date, and time of the crime in which the superhero"
        print "assisted in saving."
        print ""

        sid = getSuperheroID()

        cid = getCrimeID()

        cur = db.cursor()

        sql = "INSERT INTO supersave VALUES (%s, %s)"

        try:
                cur.execute(sql, (sid, cid))
        except (me.OperationalError,me.DataError,me.IntegrityError):
                print ""
                print "This interaction was unable to be inserted into the database."
                return

        print ""
        print "This interaction was able to be inserted into the database."
        db.commit()

# Insert a record into 'strategy'
# power used in crime

def insertStrategy():

        print "First, you must enter the name of the power involved in the crime"
        print "and the location, date, and time itself."
        print ""

        pid = getPowerID()

        cid = getCrimeID()

        cur = db.cursor()

        sql = "INSERT INTO strategy VALUES (%s, %s)"

        try:
                cur.execute(sql, (pid, cid))
        except (me.OperationalError,me.DataError,me.IntegrityError):
                print ""
                print "The power used in the crime was unable to be inserted."
                return
        
        print ""
        print "The power used in the crime was able to be inserted."
        db.commit()

# Insert a record into 'superpower'
# superheroes & the powers they possess

def insertSuperpower():

        print "You must enter the name of the superhero and the power:"
        print ""

        sid = getSuperheroID()

        pid = getPowerID()

        cur = db.cursor()

        sql = "INSERT INTO superpower (pid, sid) VALUES (%s, %s)"

        try:
                cur.execute(sql, (pid, sid))
        except (me.OperationalError,me.DataError,me.IntegrityError):
                print ""
                print ("%s cannot be associated with %s") % (sid, pid)
                return
        print ""
        print ("%s is now associated with %s") % (sid, pid)
        db.commit()

# Insert a record into 'archpower'
# archenemies & the powers they possess

def insertArchpower():

        print "You must enter the name of the archenemy and the power:"
        print ""

        aid = getArchenemyID()

        pid = getPowerID()

        cur = db.cursor()

        sql = "INSERT INTO archpower (pid, aid) VALUES (%s, %s)"

        try:
                cur.execute(sql, (pid, aid))
        except (me.OperationalError,me.DataError,me.IntegrityError):
                print ""
                print ("%s cannot be associated with %s") % (aid, pid)
                return
        
        print ""
        print ("%s is now associated with %s") % (aid, pid)
        db.commit()

# Insert a record into 'archcommit'
# archenemies & the crimes they have committed

def insertArchcommit():

        print "First, you must enter the name of the archenemy and the"
        print "location, date, and time of the crime in which the archenemy"
        print "was involved in committing."
        print ""

        aid = getArchenemyID()

        cid = getCrimeID()

        cur = db.cursor()
        
        sql = "INSERT INTO archcommit (cid, aid) VALUES (%s, %s)"

        try:
                cur.execute(sql, (cid, aid))
        except (me.OperationalError,me.DataError,me.IntegrityError):
                print ""
                print ("%s cannot be associated with %s") % (aid, cid)
                return
        print ""
        print ("%s can be associated with %s") % (aid, cid)
        db.commit()

# Updates records in the 'people' table

def updatePeople():

        cur = db.cursor()

        print("First, you must enter the first and last name of")
        print("the person you wish to update.")
        print ""

        id = getPersonID()

        print("Now, you may enter the updated field values.")
        print ""
        
        firstname = raw_input("What is the person's first name? ")

        lastname = raw_input("What is the person's last name? ")

        gender = raw_input("What is the person's gender? ")

        location = raw_input("What is the person's location? ")

        dob = raw_input("What is the person's date of birth (YYYY-MM-DD)? ")

        sql = """UPDATE people
                 SET firstname = %s, lastname = %s, gender = %s, location = %s, dob = %s
                 WHERE id = %s"""

        try:
                cur.execute(sql, (firstname, lastname, gender, location, dob, id))
        except (me.OperationalError,me.DataError):
                print ""
                print "The person's record was unable to be updated in the database."
                return
        print ""
        print "The person's record was able to be updated in the database."
        db.commit()

# Updates records in the 'superhero' table

def updateSuperhero():

        print("First, you must enter the first and last name of")
        print("the person you wish to update as well as the person's")
        print("superhero name.")
        print ""

        id = getPersonID()

        sid = getSuperheroID()

        cur = db.cursor()

        print("Now, you may enter the updated field values.")
        print ""

        name = raw_input("What is the superhero's name? ")
        print ""
        contact = raw_input("What is the superhero's contact information? ")


        sql = """UPDATE superhero
                 SET name = %s, contact = %s
                 WHERE id = %s and sid = %s"""

        try:
                cur.execute(sql, (name, contact, id, sid))
        except (me.OperationalError,me.DataError):
                print ""
                print "This superhero was not able to updated in the database."
                return
        
        print
        print "This superhero was able to be updated in the database."
        db.commit()

# Updates records in 'archenemy' table

def updateArchenemy():

        print("First, you must enter the first and last name of")
        print("the person you wish to update as well as the person's")
        print("archenemy name.")
        print ""

        id = getPersonID()

        aid = getArchenemyID()

        cur = db.cursor()

        print("Now, you may enter the updated field values.")
        print ""

        name = raw_input("What is the archenemy's name? ")

        contact = raw_input("What is the archenemy's contact information? ")


        sql = """UPDATE archenemy
                 SET name = %s, contact = %s
                 WHERE id = %s and aid = %s"""

        try:
                cur.execute(sql, (name, contact, id, aid))
        except (me.OperationalError,me.DataError):
                print ""
                print "The archenemy was not able to be updated in the database."
                return
        print
        print "The archenemy was able to be updated in the database."
        db.commit()

# Update records in 'power' table

def updatePower():

        print("First, you must enter the name of the power you wish to update.")
        print ""

        pid = getPowerID()

        cur = db.cursor()

        print("Now, you may enter the updated field values.")
        print ""

        name = raw_input("What is the name of the power? ")

        fatality = raw_input("Is the power fatal (Y/N)? ")

        description = raw_input("Describe the power: ")


        sql = """UPDATE power
                 SET name = %s, fatality = %s, description = %s
                 WHERE pid = %s"""

        try:
                cur.execute(sql, (name, fatality, description, pid))
        except (me.OperationalError,me.DataError):
                print ""
                print "The power record was unable to be updated."
                return

        print "The power record was able to be updated."
        db.commit()

# Update recods in 'crime' table

def updateCrime():

        print("First, you must enter information about the crime you wish to update.")

        cid = getCrimeID()

        cur = db.cursor()

        print("Now, you may enter the updated field values.")
        print ""

        location = raw_input("What is the location of the crime? ")

        datetime = raw_input("What is the date and time of the crime? ")

        description = raw_input("Provide a description of the crime: ")

        resolved = raw_input("Is it resolved (Y/N)?" )


        sql = """UPDATE crime
                 SET location = %s, datetime = %s, description = %s, resolved = %s
                 WHERE cid = %s"""

        try:
                cur.execute(sql, (location, datetime, description, resolved, cid))
        except (me.OperationalError,me.DataError):
                print ""
                print "The crime was unable to be updated."
                return
        print ""
        print "The crime was able to be updated."
        db.commit()

# Updates interactions in the 'fights' table
# superhero vs. archenemy

def updateInteraction():

    cur = db.cursor()

    print ""
    print "First, you must enter who is involved in the interaction."

    SuperheroID = getSuperheroID()

    ArchenemyID = getArchenemyID()

    print "Now, you may enter the updated field values."

    newSuperheroID = getSuperheroID()

    newArchenemyID = getArchenemyID()

    sql = """UPDATE fights
             SET sid = %s, aid = %s
             WHERE sid = %s AND aid = %s"""

    try:
        cur.execute(sql, (newSuperheroID, newArchenemyID, SuperheroID, ArchenemyID))
    except (me.OperationalError,me.DataError):
        print ""
        print "This interaction was not updated."

    print "This interaction was updated."
    db.commit()

# Updates the 'superpower' table
# superhero and power

def updateSuperpower():

    cur = db.cursor()

    print ""
    print "First, you must enter the superhero name and power."

    SuperheroID = getSuperheroID()

    PowerID = getPowerID()

    print "Now, you may enter the updated field values."

    newSuperheroID = getSuperheroID()

    newPowerID = getPowerID()

    sql = """UPDATE superpower
             SET sid = %s, pid = %s
             WHERE sid = %s AND pid = %s"""

    try:
        cur.execute(sql, (newSuperheroID, newPowerID, SuperheroID, PowerID))
    except (me.OperationalError,me.DataError):
        print ""
        print "This superhero and power were not updated."

    print "This superhero and power were updated."
    db.commit()

# Updates the 'archpower' table
# archenemy and power

def updateArchpower():

    cur = db.cursor()

    print ""
    print "First, you must enter the archenemy name and power."

    ArchenemyID = getArchenemyID()

    PowerID = getPowerID()

    print "Now, you may enter the updated field values."

    newArchenemyID = getArchenemyID()

    newPowerID = getPowerID()

    sql = """UPDATE archpower
             SET aid = %s, pid = %s
             WHERE aid = %s AND pid = %s"""

    try:
        cur.execute(sql, (newArchenemyID, newPowerID, ArchenemyID, PowerID))
    except (me.OperationalError,me.DataError):
        print ""
        print "This archenemy and power were not updated."

    print "This archenemy and power were updated."
    db.commit()

# Updates the 'supersave' table
# superhero and crime

def updateSupersave():

    cur = db.cursor()

    print ""
    print "First, you must enter the information about the superhero"
    print "and the crime."

    SuperheroID = getSuperheroID()

    CrimeID = getCrimeID()

    print "Now, you may enter the updated field values."

    newSuperheroID = getSuperheroID()

    newCrimeID = getCrimeID()

    sql = """UPDATE supersave
             SET sid = %s, cid = %s
             WHERE sid = %s AND cid = %s"""

    try:
        cur.execute(sql, (newSuperheroID, newCrimeID, SuperheroID, CrimeID))
    except (me.OperationalError,me.DataError):
        print ""
        print "This superhero and crime were not updated."

    print "This superhero and crime were updated."
    db.commit()

# Updates the 'archcommit' table
# archenemy and crime

def updateArchcommit():

    cur = db.cursor()

    print ""
    print "First, you must enter the information about the archenemy"
    print "and the crime."

    ArchenemyID = getArchenemyID()

    CrimeID = getCrimeID()

    print "Now, you may enter the updated field values."

    newArchenemyID = getArchenemyID()

    newCrimeID = getCrimeID()

    sql = """UPDATE archcommit
             SET aid = %s, cid = %s
             WHERE aid = %s AND cid = %s"""

    try:
        cur.execute(sql, (newArchenemyID, newCrimeID, ArchenemyID, CrimeID))
    except (me.OperationalError,me.DataError):
        print ""
        print "This archenemy and crime were not updated."

    print "This archenemy and crime were updated."
    db.commit()

# Updates the 'strategy' table
# power and crime

def updateStrategy():

    cur = db.cursor()

    print ""
    print "First, you must enter the information about the power"
    print "and the crime."

    PowerID = getPowerID()

    CrimeID = getCrimeID()

    print "Now, you may enter the updated field values."

    newPowerID = getPowerID()

    newCrimeID = getCrimeID()

    sql = """UPDATE strategy
             SET pid = %s, cid = %s
             WHERE pid = %s AND cid = %s"""

    try:
        cur.execute(sql, (newPowerID, newCrimeID, PowerID, CrimeID))
    except (me.OperationalError,me.DataError):
        print ""
        print "This power and crime were not updated."

    print "This power and crime were updated."
    db.commit()

# deletes record in 'people' table

def deletePeople():

        print("First, you must enter the first and last name of")
        print("the person you wish to delete.")
        print ""

        id = getPersonID()

        cur = db.cursor()

        print ("All records associated with the ID number %s have been deleted.") % id

        sql = "DELETE FROM people WHERE id = %s"

        cur.execute(sql, (id, ))

        db.commit()

# deletes record in 'superhero' table

def deleteSuperhero():

        print("First, you must enter the first and last name of")
        print("the person you wish to delete as well as the person's")
        print("superhero name.")
        print ""

        id = getPersonID()

        sid = getSuperheroID()

        cur = db.cursor()

        print ("All records associated with the ID number %s have been deleted.") % id

        sql = "DELETE FROM superhero WHERE id = %s and sid = %s"

        cur.execute(sql, (id, sid ))

        db.commit()

# deletes record in 'archenemy' table

def deleteArchenemy():

        print("First, you must enter the first and last name of")
        print("the person you wish to delete as well as the person's")
        print("archenemy name.")
        print ""

        id = getPersonID()

        aid = getArchenemyID()

        cur = db.cursor()

        print ("All records associated with the ID number %s have been deleted.") % id

        sql = "DELETE FROM archenemy WHERE id = %s and aid = %s "

        cur.execute(sql, (id, aid))

        db.commit()

# deletes record in 'power' table

def deletePower():

        print("First, you must enter the name of the power you wish to delete.")
        print ""

        pid = getPowerID()

        cur = db.cursor()

        print ("All records associated with the ID number %s have been deleted.") % pid

        sql = "DELETE FROM power WHERE pid = %s"

        cur.execute(sql,(pid, ))

        db.commit()

# deletes record in 'crime' table

def deleteCrime():

        print("First, you must enter the information about the crime you wish to delete.")
        print ""

        cid = getCrimeID()

        cur = db.cursor()

        print ("All records associated with the ID number %s have been deleted.") % cid

        sql = "DELETE FROM crime WHERE cid = %s"

        cur.execute(sql, (cid, ))

        db.commit()

# Deletes interactions in the 'fights' table
# Superhero vs. Archenemy

def deleteInteraction():

    print("First, you must enter the name of the superhero and the archenemy.")
    print ""

    sid = getSuperheroID()

    aid = getArchenemyID()

    cur = db.cursor()

    print ("All records associated with ID number %s and ID number %s have been deleted.") % (sid, aid)
    print ""

    sql = """DELETE FROM fights WHERE sid = %s AND aid = %s"""

    cur.execute(sql, (sid, aid))

    db.commit()

# Deletes from 'superpower' table
# Superhero and power

def deleteSuperpower():

    print("First, you must enter the name of the superhero and the power.")
    print ""

    sid = getSuperheroID()

    pid = getPowerID()

    cur = db.cursor()

    print ("All records associated with ID number %s and ID number %s have been deleted.") % (sid, pid)
    print ""

    sql = """DELETE FROM superpower WHERE sid = %s AND pid = %s"""

    cur.execute(sql, (sid, pid))

    db.commit()

# Deletes from 'archpower' table
# Archenemy and power

def deleteArchpower():

    print("First, you must enter the name of the archenemy and the power.")
    print ""

    aid = getArchenemyID()

    pid = getPowerID()

    cur = db.cursor()

    print ("All records associated with ID number %s and ID number %s have been deleted.") % (aid, pid)
    print ""

    sql = """DELETE FROM archpower WHERE aid = %s AND pid = %s"""

    cur.execute(sql, (aid, pid))

    db.commit()

# Deletes from 'supersave' table
# superhero and crime

def deleteSuperSave():

    print("First, you must enter the name of the superhero and the crime.")
    print ""

    sid = getSuperheroID()

    cid = getCrimeID()

    cur = db.cursor()

    print ("All records associated with ID number %s and ID number %s have been deleted.") % (sid, cid)
    print ""

    sql = """DELETE FROM supersave WHERE sid = %s AND cid = %s"""

    cur.execute(sql, (sid, cid))

    db.commit()

# Deletes from 'archcommit' table
# archenemy and crime

def deleteArchcommit():

    print("First, you must enter the name of the archenemy and the crime.")
    print ""

    aid = getArchenemyID()

    cid = getCrimeID()

    cur = db.cursor()

    print ("All records associated with ID number %s and ID number %s have been deleted.") % (aid, cid)
    print ""

    sql = """DELETE FROM archcommit WHERE aid = %s AND cid = %s"""

    cur.execute(sql, (aid, cid))

    db.commit()

# Deletes from 'strategy' table
# power and crime

def deleteStrategy():

    print("First, you must enter the name of the archenemy and the crime.")
    print ""

    pid = getPowerID()

    cid = getCrimeID()

    cur = db.cursor()

    print ("All records associated with ID number %s and ID number %s have been deleted.") % (pid, cid)
    print ""

    sql = """DELETE FROM strategy WHERE pid = %s AND cid = %s"""

    cur.execute(sql, (pid, cid))

    db.commit()

# This is my main function, which calls on all necessary functions.
# The menu prints in a loop until the user of the program decides to quit
# the application.

# The user may quit the application by typing: q.
if __name__ == "__main__":
        db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                                        user="navienarula", # your username
                                        passwd="kid4ever", # your password
                                        db="helpwanted") # name of the data base


        choice = "foo"

        while choice.lower()[0] != "q":

                print """
        Welcome to the HELP WANTED database! Please select one of
        the following options below to proceed. If you have any questions,
        please call N. Narula at 617-818-4686 for technical assistance.

        PEOPLE
        
        (sp) show people            (ip) insert people
        (up) update people          (dp) delete people

        (q) quit the application

        SUPERHERO
        
        {ss} show superhero         {is} insert superhero
        {us} update superhero       {ds} delete superhero

        {q} quit the application

        ARCHENEMY

        [sa] show archenemy         [ia] insert archenemy
        [ua] update archenemy       [da] delete archenemy

        [q] quit application        

        POWER

        'spo' show power            'ipo' insert power           
        'upo' update power          'dpo' delete power

        'q' quit application

        CRIME

        <sc> show crime             <ic> insert crime
        <uc> update crime           <dc> delete crime
        
        <q> quit application

        INTERACTION

        |si| show interaction       |ii| insert interaction
        |ui| update interaction     |di| delete interaction

        |sis| show interaction for specific superhero
        |sia| show interaction for specific archenemy

        |q| quit application

        SUPERHERO & POWER

        (ssp) show superhero and power       (isp) insert superhero and power
        (usp) update superhero and power     (dsp) delete superhero and power
        
        (sssp) show superhero with specific power
        (spss) show power for specific superhero

        (q) quit application

        ARCHENEMY & POWER

        {sap} show archenemy and power       {iap} insert archenemy and power
        {uap} update archenemy and power     {dap} delete archenemy and power
        
        {sasp} show archenemy with specific power
        {spsa} show power for specific archenemy
        
        {q} quit application

        SUPERHERO & CRIME

        [ssc] show superhero and crime         [isc] insert superhero and crime
        [usc] update superhero and crime       [dsc] delete superhero and crime

        [scss] show crime for specific superhero

        [q] quit application

        ARCHENEMY & CRIME

        'sac' show archenemy and crime         'iac' insert archenemy and crime
        'uac' update archenemy and crime       'dac' delete archenemy and crime

        'scsa' show crime for specific archenemy

        'q' quit application

        POWER & CRIME

        <scp> show crime and power             <icp> insert crime and power
        <ucp> update crime and power           <dcp> delete crime and power

        <scsp> show crime with specific power
        
        <q> quit application

        
        """

                choice = raw_input("> ")

                if choice.lower() == "sp":
                      printPeople()

                elif choice.lower() == "ip":
                        insertPeople()

                elif choice.lower() == "up":
                        updatePeople()

                elif choice.lower() == "dp":
                        deletePeople()

                elif choice.lower() == "ss":
                        printSuperhero()

                elif choice.lower() == "is":
                        insertSuperhero()

                elif choice.lower() == "us":
                        updateSuperhero()
                        
                elif choice.lower() == "ds":
                        deleteSuperhero()
                
                elif choice.lower() == "sa":
                        printArchenemy()

                elif choice.lower() == "ia":
                        insertArchenemy()

                elif choice.lower() == "ua":
                        updateArchenemy()
                        
                elif choice.lower() == "da":
                        deleteArchenemy()

                elif choice.lower() == "spo":
                        printPower()

                elif choice.lower() == "ipo":
                        insertPower()

                elif choice.lower() == "upo":
                        updatePower()
                        
                elif choice.lower() == "dpo":
                        deletePower()

                elif choice.lower() == "sc":
                        printCrime()

                elif choice.lower() == "ic":
                        insertCrime()

                elif choice.lower() == "uc":
                        updateCrime()
                        
                elif choice.lower() == "dc":
                        deleteCrime()

                elif choice.lower() == "si":
                        printInteraction()

                elif choice.lower() == "ii":
                        insertInteraction()

                elif choice.lower() == "ui":
                    updateInteraction()

                elif choice.lower() == "di":
                    deleteInteraction()

                elif choice.lower() == "sis":
                        printInteractionSup()

                elif choice.lower() == "sia":
                        printInteractionArch()

                elif choice.lower() == "ssp":
                        printSuperpower()

                elif choice.lower() == "isp":
                        insertSuperpower()

                elif choice.lower() == "usp":
                    updateSuperpower()

                elif choice.lower() == "dsp":
                    deleteSuperpower()

                elif choice.lower() == "spss":
                        printAllPowerSup()

                elif choice.lower() == "sssp":
                        printAllSupPower()

                elif choice.lower() == "sap":
                    printArchpower()

                elif choice.lower() == "sasp":
                        printAllPowerArch()

                elif choice.lower() == "spsa":
                        printAllArchPower()

                elif choice.lower() == "iap":
                        insertArchpower()

                elif choice.lower() == "uap":
                        updateArchpower()

                elif choice.lower() == "dap":
                        deleteArchpower()

                elif choice.lower() == "ssc":
                    printSupersave()

                elif choice.lower() == "isc":
                        insertSupersave()

                elif choice.lower() == "usc":
                        updateSupersave()

                elif choice.lower() == "dsc":
                        deleteSuperSave()

                elif choice.lower() == "scss":
                        printSupersaveSup()

                elif choice.lower() == "sac":
                        printArchcommit()

                elif choice.lower() == "scsa":
                        printArchcommitArch()

                elif choice.lower() == "iac":
                        insertArchcommit()

                elif choice.lower() == "uac":
                        updateArchcommit()

                elif choice.lower() == "dac":
                        deleteArchcommit()

                elif choice.lower() == "scp":
                        printStrategy()

                elif choice.lower() == "scsp":
                        printStrategyPow()

                elif choice.lower() == "icp":
                        insertStrategy()

                elif choice.lower() == "ucp":
                        updateStrategy()

                elif choice.lower() == "dcp":
                        deleteStrategy()

                elif choice.lower() == "q":
                        print("Have a good day! See you next time around.")

                else:
                        print("Sorry! That does not seem to be an option.")
        

