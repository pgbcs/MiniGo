.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [LPerson; from Label2 to Label3
	iconst_5
	anewarray Person
	dup
	iconst_0
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Alice"
	putfield Person/name Ljava/lang/String;
	dup
	bipush 20
	putfield Person/age I
	aastore
	dup
	iconst_1
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Bob"
	putfield Person/name Ljava/lang/String;
	dup
	bipush 25
	putfield Person/age I
	aastore
	dup
	iconst_2
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Charlie"
	putfield Person/name Ljava/lang/String;
	dup
	bipush 30
	putfield Person/age I
	aastore
	dup
	iconst_3
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "David"
	putfield Person/name Ljava/lang/String;
	dup
	bipush 35
	putfield Person/age I
	aastore
	dup
	iconst_4
	new Person
	dup
	invokespecial Person/<init>()V
	dup
	ldc "Eve"
	putfield Person/name Ljava/lang/String;
	dup
	bipush 40
	putfield Person/age I
	aastore
	astore_1
	aload_1
	iconst_2
	aaload
	getfield Person/age I
	invokestatic io/putInt(I)V
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
