.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a [[I
.field static b [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/b [I
	iconst_1
	iaload
	invokestatic io/putInt(I)V
Label3:
	nop
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	iconst_2
	iconst_2
	multianewarray [[I 2
	dup
	iconst_0
	aaload
	iconst_0
	iconst_1
	iastore
	dup
	iconst_0
	aaload
	iconst_1
	iconst_2
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	iconst_4
	iastore
	putstatic MiniGoClass/a [[I
	getstatic MiniGoClass/a [[I
	iconst_0
	aaload
	putstatic MiniGoClass/b [I
Label1:
	return
.limit stack 5
.limit locals 0
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
