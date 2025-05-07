.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo(LPerson;)V
.var 0 is p LPerson; from Label0 to Label1
Label0:
Label2:
	aload_0
	bipush 10
	putfield Person/age I
Label3:
	nop
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is p LPerson; from Label2 to Label3
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Alice"
	putfield Person/name Ljava/lang/String;
	dup
	iconst_5
	putfield Person/age I
	astore_1
	aload_1
	invokestatic MiniGoClass/foo(LPerson;)V
	aload_1
	getfield Person/age I
	invokestatic io/putInt(I)V
Label3:
	nop
Label1:
	return
.limit stack 3
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
