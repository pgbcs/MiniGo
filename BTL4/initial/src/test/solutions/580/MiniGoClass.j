.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is p LPerson; from Label2 to Label3
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "John"
	putfield Person/name Ljava/lang/String;
	dup
	bipush 30
	putfield Person/age I
	astore_1
.var 2 is olderPerson LPerson; from Label2 to Label3
	aload_1
	iconst_5
	invokevirtual Person/getOlder(I)LPerson;
	astore_2
	aload_2
	getfield Person/age I
	invokestatic io/putInt(I)V
Label3:
	nop
Label1:
	return
.limit stack 3
.limit locals 3
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
