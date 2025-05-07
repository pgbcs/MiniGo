.source Person.java
.class public Person
.super java.lang.Object
.field name Ljava/lang/String;
.field age I

.method public <init>()V
.var 0 is this LPerson; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aconst_null
	putfield Person/name Ljava/lang/String;
	aload_0
	iconst_0
	putfield Person/age I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public getOlder(I)LPerson;
.var 0 is this LPerson; from Label0 to Label1
.var 1 is years I from Label0 to Label1
Label0:
Label2:
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	aload_0
	getfield Person/name Ljava/lang/String;
	putfield Person/name Ljava/lang/String;
	dup
	aload_0
	getfield Person/age I
	iload_1
	iadd
	putfield Person/age I
	areturn
Label3:
	nop
Label1:
.limit stack 5
.limit locals 2
.end method
