from django.db import models

class Organization(models.Model):
	Organizationcode = models.CharField (max_length=20)
	name = models.CharField (max_length=20)
	description = models.CharField (max_length=20)
	date_joined = models.CharField (max_length=20)
	address1 = models.CharField (max_length=20, default="")
	address2 = models.CharField (max_length=20)
	city = models.CharField (max_length=20)
	state = models.CharField (max_length=20)
	zipcode = models.CharField (max_length=20)
	phone_number = models.CharField (max_length=20)

	def __str__(self):
		return self.Organizationcode
		return self.name
		return self.description
		return self.date_joined
		return self.address1
		return self.address2
		return self.city
		return self.state
		return self.zipcode
		return self.phone_number

class Userinfo(models.Model):
	Username = models.CharField (max_length=20)
	firstname = models.CharField (max_length=20)
	middlename = models.CharField (max_length=20)
	lastname = models.CharField (max_length=20)
	email = models.CharField (max_length=20)
	address1 = models.CharField (max_length=20)
	address2 = models.CharField (max_length=20)
	city = models.CharField (max_length=20)
	state = models.CharField (max_length=20)
	zipcode = models.CharField (max_length=20)
	employername = models.CharField (max_length=20)

	def __str__(self):
		return self.username
		return self.firstname
		return self.middlename
		return self.lastname
		return self.email
		return self.address1
		return self.address2
		return self.city
		return self.state
		return self.zipcode
		return self.employername

class SubcriptionType(models.Model):
	Subscriptiontypecode = models.CharField (max_length=20)
	subscriptiontypename = models.CharField (max_length=20)

	def __str__(self):
		return self.subscriptiontypecode
		return self.subscriptiontypename

class Service(models.Model):
	Servicecode = models.CharField (max_length=20)
	servicename = models.CharField (max_length=20)
	description = models.CharField (max_length=20)
	premium = models.CharField (max_length=20)
	allocation = models.CharField (max_length=20)

	def __str__(self):
		return self.Servicecode
		return self.servicename
		return self.description
		return self.premium
		return self.allocation

class Subscriber(models.Model):
	SubscriberID = models.CharField (max_length=20)
	requestdate = models.CharField (max_length=20)
	startdate = models.CharField (max_length=20)
	enddate = models.CharField (max_length=20)
	motifofcancellation = models.CharField (max_length=20)
	BeneficiaryID = models.CharField (max_length=20)

	username = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
	subscriptiontypecode = models.ForeignKey(SubcriptionType, on_delete=models.CASCADE)
	servicecode = models.ForeignKey(Service, on_delete=models.CASCADE)

	def __str__(self):
		return self.SubscriberID
		return self.Username
		return self.Subscriptiontypecode
		return self.Servicecode
		return self.requestdate
		return self.startdate
		return self.enddate
		return self.motifofcancellation
		return self.BeneficiaryID

class OrganizationMember(models.Model):
	startdate = models.CharField (max_length=20)
	enddate = models.CharField (max_length=20)
	nativecountry = models.CharField (max_length=20)
	citizenship = models.CharField (max_length=20)
	isdelegate = models.CharField (max_length=20)

	organizationcode = models.ForeignKey(Organization, on_delete=models.CASCADE)
	subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

	def __str__(self):
		return self.SubscriberID
		return self.startdate
		return self.enddate
		return self.nativecountry
		return self.citizenship
		return self.isdelegate

class Office(models.Model):
	Officecode = models.CharField (max_length=20)
	officename = models.CharField (max_length=20)
	attribution = models.CharField (max_length=20)

	def __str__(self):
		return self.Officecode
		return self.officename
		return self.attribution

class Officer(models.Model):
	startdate = models.CharField (max_length=20)
	enddate = models.CharField (max_length=20)

	subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
	officecode = models.ForeignKey(Office, on_delete=models.CASCADE, default="")

	def __str__(self):
		return self.startdate
		return self.enddate

class TransferredSubscription(models.Model):
	transferID = models.CharField (max_length=20)
	transferfrom = models.CharField (max_length=20)
	transferto = models.CharField (max_length=20)
	requestdate = models.CharField (max_length=20)
	transferdate = models.CharField (max_length=20)

	subscriberID = models.ForeignKey(Subscriber, on_delete=models.CASCADE)

	def __str__(self):
		return self.transferID
		return self.transferfrom
		return self.transferto
		return self.requestdate
		return self.transferdate


