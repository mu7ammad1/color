"use server";

import { createClient } from "@/lib/server";

// تهيئة عميل Supabase
const supabase = createClient();

// دالة Server Action لإضافة أو تحديث الإعجاب
export async function handleInsertLike(id: string) {
  try {
    // تنفيذ الاستعلام لإضافة أو تحديث سجل الإعجاب

    const { data, error } = await (
      await supabase
    )
      .from("likes_count")
      .insert([{ likes_count: id }])
      .select();

    if (error) {
      console.error("Error inserting/updating like:", error);
    } else {
      console.log("Like added or updated successfully", data);
    }
  } catch (error) {
    console.error("Error inserting like:", error);
  }
}
