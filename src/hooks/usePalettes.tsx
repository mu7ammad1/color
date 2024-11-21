"use client";
import { useState } from "react";
import { createClient } from "@/lib/client";

interface Palette {
  id: string;
  color1: string;
  color2: string;
  color3: string;
  color4: string;
  created_at: string;
  likes_count: number;
}

export function usePalettes(limit: 20, from: `random_colors_view` | `colors`) {
  const [palettes, setPalettes] = useState<Palette[]>([]);
  const [offset, setOffset] = useState(0);
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  const fetchPalettes = async () => {
    if (loading || !hasMore) return;

    setLoading(true);
    const supabase = await createClient();

    const { data, error } = await supabase
      .from(from)
      .select("*,likes_count (id,likes_count)")
      .range(offset, offset + limit - 1);

    if (error) {
      console.error("Error fetching palettes:", error);
    } else {
      setPalettes((prev) => [...prev, ...data]);
      setOffset((prevOffset) => prevOffset + limit);
      if (data.length < limit) setHasMore(false);
    }

    setLoading(false);
  };

  return { palettes, loading, hasMore, fetchPalettes };
}

export function usePopular(limit = 20) {
  const [palettes, setPalettes] = useState<Palette[]>([]);
  const [offset, setOffset] = useState(0);
  const [loading, setLoading] = useState(false);
  const [hasMore, setHasMore] = useState(true);

  const fetchPalettes = async () => {
    if (loading || !hasMore) return;

    setLoading(true);
    const supabase = await createClient();

    try {
      const { data, error } = await supabase
        .from("colors")
        .select("*,likes_count (id,likes_count)")
        .range(offset, offset + limit - 1);

      if (error) {
        throw error; // رفع الخطأ إلى الكود الخارجي
      }

      if (data) {
        setPalettes((prev) => [...prev, ...data]);
        setOffset((prevOffset) => prevOffset + limit);
        if (data.length < limit) setHasMore(false);
      }
    } catch (error) {
      console.error("Error fetching palettes:", error);
    } finally {
      setLoading(false);
    }
  };

  return { palettes, loading, hasMore, fetchPalettes };
}
