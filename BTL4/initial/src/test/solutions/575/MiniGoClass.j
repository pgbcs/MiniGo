.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static foo()[I
Label0:
Label2:
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
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
	areturn
Label3:
	nop
Label1:
.limit stack 4
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is b [F from Label2 to Label3
	invokestatic MiniGoClass/foo()[I
	dup
	ifnull Label5
.var 2 is temp [I from Label2 to Label3
	astore_2
	iconst_5
	newarray float
	dup
	iconst_0
	aload_2
	iconst_0
	iaload
	i2f
	fastore
	dup
	iconst_1
	aload_2
	iconst_1
	iaload
	i2f
	fastore
	dup
	iconst_2
	aload_2
	iconst_2
	iaload
	i2f
	fastore
	dup
	iconst_3
	aload_2
	iconst_3
	iaload
	i2f
	fastore
	dup
	iconst_4
	aload_2
	iconst_4
	iaload
	i2f
	fastore
	goto Label4
Label5:
	pop
	aconst_null
Label4:
	astore_1
	aload_1
	iconst_0
	faload
	invokestatic io/putFloat(F)V
Label3:
	nop
Label1:
	return
.limit stack 5
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
