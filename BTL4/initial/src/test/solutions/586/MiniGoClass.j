.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static createPerson(Ljava/lang/String;I)LPerson;
.var 0 is name Ljava/lang/String; from Label0 to Label1
.var 1 is age I from Label0 to Label1
Label0:
Label2:
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	aload_0
	putfield Person/name Ljava/lang/String;
	dup
	iload_1
	putfield Person/age I
	areturn
Label3:
	nop
Label1:
.limit stack 3
.limit locals 2
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is p LPerson; from Label2 to Label3
	ldc "Alice"
	bipush 25
	invokestatic MiniGoClass/createPerson(Ljava/lang/String;I)LPerson;
	astore_1
	aload_1
	getfield Person/name Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	getfield Person/age I
	invokestatic io/putIntLn(I)V
Label3:
	nop
Label1:
	return
.limit stack 2
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
