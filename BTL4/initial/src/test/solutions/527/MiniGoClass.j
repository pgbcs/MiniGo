.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is b I from Label2 to Label3
	iconst_5
	istore_1
.var 2 is c [[[I from Label2 to Label3
	iconst_3
	iconst_2
	iconst_2
	multianewarray [[[I 3
	dup
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	dup
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	dup
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_0
	iconst_3
	iastore
	dup
	iconst_0
	aaload
	iconst_1
	aaload
	iconst_1
	iconst_4
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	aaload
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	aaload
	iconst_1
	bipush 6
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	aaload
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	aaload
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	aaload
	iconst_0
	aaload
	iconst_0
	bipush 9
	iastore
	dup
	iconst_2
	aaload
	iconst_0
	aaload
	iconst_1
	bipush 10
	iastore
	dup
	iconst_2
	aaload
	iconst_1
	aaload
	iconst_0
	bipush 11
	iastore
	dup
	iconst_2
	aaload
	iconst_1
	aaload
	iconst_1
	bipush 12
	iastore
	astore_2
	aload_2
	iconst_0
	aaload
	iconst_0
	aaload
	iconst_1
	iaload
	invokestatic io/putInt(I)V
Label3:
	nop
Label1:
	return
.limit stack 6
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
