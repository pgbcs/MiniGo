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
	dup
	iconst_3
	newarray int
	dup
	iconst_0
	bipush 90
	iastore
	dup
	iconst_1
	bipush 80
	iastore
	dup
	iconst_2
	bipush 70
	iastore
	putfield Person/scores [I
	astore_1
	aload_1
	getfield Person/scores [I
	iconst_0
	iaload
	i2f
	invokestatic io/putFloat(F)V
Label3:
	nop
Label1:
	return
.limit stack 6
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
