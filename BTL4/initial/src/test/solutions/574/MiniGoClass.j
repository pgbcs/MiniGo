.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [I from Label2 to Label3
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	astore_1
.var 2 is b [[F from Label2 to Label3
	iconst_2
	iconst_5
	multianewarray [[F 2
	dup
	iconst_0
	aaload
	iconst_0
	ldc 1.0
	fastore
	dup
	iconst_0
	aaload
	iconst_1
	ldc 2.0
	fastore
	dup
	iconst_0
	aaload
	iconst_2
	ldc 3.0
	fastore
	dup
	iconst_0
	aaload
	iconst_3
	ldc 4.0
	fastore
	dup
	iconst_0
	aaload
	iconst_4
	ldc 5.0
	fastore
	dup
	iconst_1
	aaload
	iconst_0
	ldc 6.0
	fastore
	dup
	iconst_1
	aaload
	iconst_1
	ldc 7.0
	fastore
	dup
	iconst_1
	aaload
	iconst_2
	ldc 8.0
	fastore
	dup
	iconst_1
	aaload
	iconst_3
	ldc 9.0
	fastore
	dup
	iconst_1
	aaload
	iconst_4
	ldc 10.0
	fastore
	astore_2
	aload_2
	iconst_0
	aload_1
	dup
	ifnull Label5
.var 3 is temp [I from Label2 to Label3
	astore_3
	iconst_5
	newarray float
	dup
	iconst_0
	aload_3
	iconst_0
	iaload
	i2f
	fastore
	dup
	iconst_1
	aload_3
	iconst_1
	iaload
	i2f
	fastore
	dup
	iconst_2
	aload_3
	iconst_2
	iaload
	i2f
	fastore
	dup
	iconst_3
	aload_3
	iconst_3
	iaload
	i2f
	fastore
	dup
	iconst_4
	aload_3
	iconst_4
	iaload
	i2f
	fastore
	goto Label4
Label5:
	pop
	aconst_null
Label4:
	aastore
	aload_2
	iconst_0
	aaload
	iconst_0
	faload
	invokestatic io/putFloat(F)V
Label3:
	nop
Label1:
	return
.limit stack 8
.limit locals 4
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
