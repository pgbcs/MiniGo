.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a [I
.field static b [F

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/b [F
	iconst_0
	faload
	invokestatic io/putFloat(F)V
Label3:
	nop
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
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
	putstatic MiniGoClass/a [I
	getstatic MiniGoClass/a [I
	dup
	ifnull Label3
.var 0 is temp [I from Label0 to Label1
	astore_0
	iconst_5
	newarray float
	dup
	iconst_0
	aload_0
	iconst_0
	iaload
	i2f
	fastore
	dup
	iconst_1
	aload_0
	iconst_1
	iaload
	i2f
	fastore
	dup
	iconst_2
	aload_0
	iconst_2
	iaload
	i2f
	fastore
	dup
	iconst_3
	aload_0
	iconst_3
	iaload
	i2f
	fastore
	dup
	iconst_4
	aload_0
	iconst_4
	iaload
	i2f
	fastore
	goto Label2
Label3:
	pop
	aconst_null
Label2:
	putstatic MiniGoClass/b [F
Label1:
	return
.limit stack 5
.limit locals 1
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
