.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is s LStudent; from Label2 to Label3
	new Student
	dup
	invokespecial Student/<init>()V
	dup
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "John"
	putfield Person/name Ljava/lang/String;
	dup
	bipush 20
	putfield Person/age I
	putfield Student/person LPerson;
	dup
	bipush 90
	putfield Student/grade I
	astore_1
	aload_1
	getfield Student/person LPerson;
	getfield Person/name Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
	nop
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
