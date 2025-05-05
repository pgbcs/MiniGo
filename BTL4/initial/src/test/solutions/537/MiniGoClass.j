.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [[Ljava/lang/String; from Label2 to Label3
	iconst_2
	iconst_2
	multianewarray [[Ljava/lang/String; 2
	dup
	iconst_0
	aaload
	iconst_0
	ldc "abc"
	aastore
	dup
	iconst_0
	aaload
	iconst_1
	ldc "hello"
	aastore
	dup
	iconst_1
	aaload
	iconst_0
	ldc "ghi"
	aastore
	dup
	iconst_1
	aaload
	iconst_1
	ldc "jkl"
	aastore
	astore_1
	aload_1
	iconst_0
	aaload
	iconst_1
	aaload
	ldc "hello"
	invokevirtual java/lang/String.compareTo(Ljava/lang/String;)I
	ifne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	aload_1
	iconst_0
	aaload
	iconst_1
	ldc "world"
	aastore
	aload_1
	iconst_0
	aaload
	iconst_1
	aaload
	ldc "hello"
	invokevirtual java/lang/String.compareTo(Ljava/lang/String;)I
	ifne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBoolLn(Z)V
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
