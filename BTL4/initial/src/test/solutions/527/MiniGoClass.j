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
	iconst_1
	multianewarray [[[I 3
	iconst_3
	iconst_2
	iconst_1
	multianewarray [[[I 3
	dup
	iconst_0
	iaload
	iconst_0
	iaload
	iconst_0
	iconst_1
	iastore
	dup
	iconst_0
	iaload
	iconst_1
	iaload
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iaload
	iconst_0
	iaload
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	iaload
	iconst_1
	iaload
	iconst_0
	bipush 7
	iastore
	dup
	iconst_2
	iaload
	iconst_0
	iaload
	iconst_0
	bipush 9
	iastore
	dup
	iconst_2
	iaload
	iconst_1
	iaload
	iconst_0
	bipush 11
	iastore
	astore_2
Label3:
Label1:
	return
.limit stack 9
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
