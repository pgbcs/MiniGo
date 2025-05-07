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

.method public greet(Ljava/lang/String;)V
.var 0 is this LPerson; from Label0 to Label1
.var 1 is name Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	dup
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	dup
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	dup
	ldc "Hello, "
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	dup
	aload_1
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	dup
	ldc "! My name is "
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	dup
	aload_0
	getfield Person/name Ljava/lang/String;
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
	nop
Label1:
	return
.limit stack 9
.limit locals 2
.end method
