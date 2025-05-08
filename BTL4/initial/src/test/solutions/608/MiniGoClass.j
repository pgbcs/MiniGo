.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static getPerson()LPerson;
Label0:
Label2:
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Alice"
	putfield Person/name Ljava/lang/String;
	dup
	bipush 20
	putfield Person/age I
	areturn
Label3:
	nop
Label1:
.limit stack 3
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a LPerson; from Label2 to Label3
	invokestatic MiniGoClass/getPerson()LPerson;
	astore_1
	aload_1
	getfield Person/age I
	invokestatic io/putInt(I)V
Label3:
	nop
Label1:
	return
.limit stack 1
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
