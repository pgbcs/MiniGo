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
	new java/lang/StringBuilder
	dup
	invokespecial java/lang/StringBuilder/<init>()V
	dup
	aload_1
	iconst_0
	aaload
	iconst_1
	aaload
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	dup
	ldc " "
	invokevirtual java/lang/StringBuilder/append(Ljava/lang/String;)Ljava/lang/StringBuilder;
	invokevirtual java/lang/StringBuilder/toString()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
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
	invokestatic io/putString(Ljava/lang/String;)V
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
