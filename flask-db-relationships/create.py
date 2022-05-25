from app import db, Countries, Cities

db.create_all() # Creates all table classes defined

uk = Countries(name = 'United Kingdom') #Add example to countries table
nz = Countries(name = 'New Zealand')
sp = Countries(name = 'Spain')
db.session.add(uk)
db.session.add(nz)
db.session.add(sp)
db.session.commit()


# Here we reference the country that london belongs to useing 'country', this is what we named the backref variable in db.relationship()
ldn = Cities(name='London', country = uk)
mcr = Cities(name='Manchester', country = uk)
auck = Cities(name = 'Auckland', country = nz)
mad = Cities(name = 'Madrid', country = sp)

db.session.add(mad)
db.session.add(auck)
db.session.add(ldn)
db.session.add(mcr)
db.session.commit()

print(f"Cities in the UK are: {uk.cities[0].name}, {uk.cities[1].name}")
print(f"London's country is: {ldn.country.name}")
print(f"Manchester's country is: {ldn.country.name}")
print(f"Cities in New Zealand are: {nz.cities[0].name}")
print(f"Cities in Spain are: {sp.cities[0].name}")

