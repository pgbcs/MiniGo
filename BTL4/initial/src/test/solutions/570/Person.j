.source Person.java
.class public Person
.super java.lang.Object
.field name Ljava/lang/String;
.field age I
.field scores [I

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
	aload_0
	aconst_null
	putfield Person/scores [I
Label1:
	return
.limit stack 2
.limit locals 1
.end method
